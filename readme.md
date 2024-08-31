# Harmonized MRI

## Overview

Harmonized MRI is an initiative aimed at creating a centralized resource for Pulseq projects, enabling researchers and developers to easily share and discover new developments in the field of magnetic resonance imaging (MRI). The website provides a curated list of Pulseq projects, detailed information about each project, and resources to help users get started with Pulseq.

[Visit the website](https://harmonizedmri.github.io/)

## Features

- **Project Listings:** A searchable and filterable list of Pulseq projects.
- **Project Details:** Detailed pages for each project, including descriptions, goals, and resources.
- **Community Contributions:** Guidelines for contributing new projects to the list.

## Getting Started with the Website

To explore the projects or contribute to the initiative, visit the [Harmonized MRI website](https://harmonizedmri.github.io/).

If you are a developer and want to contribute to the website's development, follow the instructions below to set up the project locally.

## Development Setup

### Prerequisites

Ensure you have the following installed:

- **Ruby**: Version `2.5.0` or higher
- **Jekyll**: Version `4.3.3` or higher
- **Bundler**: Version `2.1.4` or higher

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/HarmonizedMRI/HarmonizedMRI.github.io.git
    cd HarmonizedMRI.github.io
    ```

2. Install Ruby and Bundler dependencies:
    ```bash
    bundle install
    ```

3. Serve the site locally with live reload:
    ```bash
    bundle exec jekyll serve --livereload --port 4001
    ```

4. Open your web browser and go to `http://localhost:4001/` to view the site.

### Customizing Layouts and Styles

If you need to customize the layout or styles:

1. Locate the layout files in the theme:
    ```bash
    bundle info --path minima
    ```
   
2. Copy the necessary layout files (e.g., `post.html`, `page.html`) into the `_layouts` directory of your project:
    ```bash
cp $(bundle info --path minima)/_layouts/post.html ./_layouts/
    ```

3. Edit the copied files to customize the layout as needed.

### Troubleshooting

If you encounter issues during setup, refer to the following resources:

- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [Jekyll Installation Guide for Ubuntu](https://jekyllrb.com/docs/installation/ubuntu/)

Common troubleshooting steps include:

- **Installing Ruby and Build Essentials**:
    ```bash
    sudo apt-get install ruby-full build-essential zlib1g-dev
    ```

- **Setting up Gem Path for Non-Root Installations**:
    ```bash
    echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
    echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
    echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc
    source ~/.bashrc
    ```

- **Uninstalling the Apt Version of Jekyll**:
    ```bash
    PACKAGES="$(dpkg -l | grep jekyll | cut -d' ' -f3 | xargs)"
    sudo apt remove --purge $PACKAGES
    sudo apt autoremove
    sudo gem install jekyll bundler
    ```

### Contributing

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-branch-name
    ```
3. Make your changes and commit them:
    ```bash
    git commit -m "Description of changes"
    ```
4. Push to your fork:
    ```bash
    git push origin feature-branch-name
    ```
5. Open a pull request in the main repository.

### License

This project is licensed under the [MIT License](LICENSE.md).
