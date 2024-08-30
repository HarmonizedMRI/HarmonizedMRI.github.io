import os
import pandas as pd
import io
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from googleapiclient.errors import HttpError
import re

# Path to your credentials file
# CREDENTIALS_FILE = '/home/ryan/Projects/HarmonizedMRI.github.io/pulseq-website-automation-8fad3674cc42.json'
CREDENTIALS_FILE = 'credentials.json'
SCOPES = ['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/spreadsheets.readonly']

# Google Sheet ID and range
SHEET_ID = '1s9nLnwGYtpg5Djc2GMCPq2rG4mlq_Ngy6_uGgBuvdII'
RANGE_NAME = 'Form Responses 1!A:G'  # Adjust according to your sheet structure

# Destination folder for logos
LOGO_FOLDER = 'assets/logos'


def authenticate_google_services():
    credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, SCOPES)
    gc = gspread.authorize(credentials)
    return credentials, gc


def get_google_sheet_data(gc):
    sh = gc.open_by_key(SHEET_ID)
    worksheet = sh.worksheet('Form Responses 1')
    return worksheet.get_all_values()


def extract_file_id(url):
    # Match the file ID in the URL
    match = re.search(r'/d/([a-zA-Z0-9_-]+)', url)
    if not match:
        match = re.search(r'id=([a-zA-Z0-9_-]+)', url)
    return match.group(1) if match else None


def download_image_from_drive(credentials, url, destination):
    drive_service = build('drive', 'v3', credentials=credentials)
    file_id = extract_file_id(url)
    if file_id is None:
        print(f"Failed to extract file ID from URL: {url}")
        return
    try:
        request = drive_service.files().get_media(fileId=file_id)
        fh = io.FileIO(destination, 'wb')
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while not done:
            status, done = downloader.next_chunk()
    except HttpError as error:
        print(f"An error occurred: {error}")
        print(f"Failed to download image from URL: {url}")


def update_projects_csv(data):
    # Define column mappings
    column_mapping = {
        'Timestamp': 'timestamp',
        'Project title': 'title',
        'Project contact email': 'contact',
        'Project URL': 'url',
        'Category': 'category',
        'Description': 'description',
        'Project logo': 'logo'
    }

    # Reorder columns according to the existing CSV structure
    reordered_data = [
        [row[0], row[1], row[2], row[3], row[4], row[5], row[6]]  # No default 'false' here
        for row in data[1:]
    ]

    # Convert the data to a DataFrame and rename columns
    df = pd.DataFrame(reordered_data, columns=[column_mapping[col] for col in data[0]])

    # Load existing CSV
    current_projects = pd.read_csv('_data/projects.csv')

    # Add 'featured' column if not present in the current CSV
    if 'featured' not in current_projects.columns:
        current_projects['featured'] = 'false'

    # Ensure new data has the same columns as existing data
    df = df[current_projects.columns[:-1]]  # Exclude 'featured' from new data
    df['featured'] = 'false'  # Set default 'featured' value for new entries

    # Concatenate, deduplicate, and save
    updated_projects = pd.concat([current_projects, df]).drop_duplicates(subset=['title', 'contact', 'url']).reset_index(drop=True)
    updated_projects.to_csv('_data/projects.csv', index=False)


def main():
    credentials, gc = authenticate_google_services()
    sheet_data = get_google_sheet_data(gc)

    for row in sheet_data[1:]:  # Skip header row
        timestamp, title, contact, url, category, description, logo_url = row
        logo_filename = os.path.join(LOGO_FOLDER, f"{title.replace(' ', '_')}.png")

        if not os.path.exists(logo_filename):
            download_image_from_drive(credentials, logo_url, logo_filename)

        row[6] = f"/assets/logos/{title.replace(' ', '_')}.png"

    update_projects_csv(sheet_data)


if __name__ == '__main__':
    main()
