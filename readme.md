# Practice writing Jekyll web page

Currently working in ./mysite2/.
To preview (serve) the site locally, do:
```
bundle exec jekyll serve --livereload --port 4001
```

and go to http://localhost:4001/ in a web browser

Plan:
1. maintain list of user Pulseq projects in .csv or yaml file
2. List on dedicated page (not home)

# Customize a layout

1. Locate theme's layout files, e.g.,
    ```
    bundle info --path minima
    ```
2. Place copy of `/home/jon/gems/gems/minima-2.5.1/_layouts/post.html` in `./_layouts/`
3. Edit, and that's it :)

Do the same with page.html, etc


# Troubleshooting installation

https://jekyllrb.com/docs/  
https://jekyllrb.com/docs/installation/ubuntu/

Some of these need to be installed once as root, probably:

```
sudo apt-get install ruby ruby-all-dev
```

and some as non-root **and in the site folder**, e.g.:
```
gem install jekyll bundler
bundle add webrick

```

## This finally may have worked


### From https://jekyllrb.com/docs/installation/ubuntu/

```
sudo apt-get install ruby-full build-essential zlib1g-dev
```

Avoid installing RubyGems packages (called gems) as the root user. 
Instead, set up a gem installation directory for your user account. 
The following commands will add environment variables to your ~/.bashrc file to configure the gem installation path:

```
echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

Finally, install Jekyll and Bundler (NOT as root, and **probably in the web site folder**):

```
gem install jekyll bundler    % NOT as root
```


### From https://stackoverflow.com/questions/68220028/undefined-method-delegate-method-as-for-jekylldropscollectiondropclass-n

Uninstall the apt version of jekyll with:

```
PACKAGES="$(dpkg -l |grep jekyll|cut -d" " -f3|xargs )"
sudo apt remove --purge $PACKAGES
```

IMPORTANT! Clean-up your dependency libs after uninstalling all debian packages:

```
sudo apt autoremove
```

Then install all needed jekyll packages via gem, e.g.:
```
sudo gem install jekyll jekyll-feed jekyll-gist jekyll-paginate jekyll-sass-converter jekyll-coffeescript
```

Then in your project directory do:

```
bundle update
```


## Create a test site and host it locally

1. Create new Jekyll site in ./myblog:
```
jekyll new myblog
```

2. Change into your new directory:
```
cd myblog
```

3. Build the site and make it available on a local server.
```
bundle exec jekyll serve --livereload --port 4001
```
4. Load in browser: navigate to http://localhost:4001/



## Download a new template and test it

1. Download, extract, and navigate to folder

2. Get dependencies:
```
bundle install
```

3. Host the site locally:
```
bundle exec jekyll serve --livereload --port 4001
```
