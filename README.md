[![YK logo](static/img/yodaKode-sml.png)](https://github.com/roeszler)

Site URL: https://thorin-flask-app-sr.herokuapp.com/about
GitHub Repository: https://github.com/roeszler/thorin-and-co

## Creating and running a Flask application.

* $ Pip3 install flask
* $ touch run.py
  * from flask import Flask (capital F indicates its a class name)
  * app = Flask(__name__)
  * @app.route(“/“)
  * def index():
	    return “Hello, World!”

* python3 run.py
* ctrl + C (exits the terminal)

## How to deploy our project using Heroku.

```
$ npm install -g heroku
$ heroku login -i
```
1. Have created a Heroku app
```
$ heroku apps
$ heroku apps:rename thorn-flask-app-stuart --app thorn-flask-app-sr
```
2. Link our local Git repository to Heroku
```
$ git status
$ git add -A
$ git status
$ git remote -v

$ git remote add heroku https://git.heroku.com/thorin-flask-app-sr.git
$ git remote -v
```
3. Create a 'requirements.txt' file, which contains a list of our Python dependencies
```
$ pip3 freeze --local > requirements.txt
$ git add -A
$ git commit -m "add requirements.txt"
$ git push -u heroku main
```

4. Create heroku Procfile
A Procfile is a Heroku-specific type of file that tells Heroku how to run our project:
```
$ echo web: python run.py > Procfile
```
What this line does, is tells Heroku that it's going to be a web process, and the command to run our application is 'python run.py'
```
$ git add Procfile
$ git commit -m "add Procfile"
$ git push
```
5. View log file 
```
$ heroku logs --tail --app APP-NAME
$ heroku logs --tail --app thorin-flask-app-sr
```

6. Add hidden / secret content
We need to add any hidden environment variables, or Config Vars, within our App Settings.

1. Reveal coffin vars (same as @ bottom of run.py file):

IP 			0.0.0.0
PORT 		5000
SECRET_KEY 	secret_flash_key

more > view logs
more > restart dynos

7. Connect directly to gitHub with automatic deploys and remove remote update link
```
$ git remote rm heroku
$ git remote -v

$ git add -A && git commit -m "push to git hub"
$ git push origin main
```

---

# Suggestions for a good README

https://www.makeareadme.com/#suggestions-for-a-good-readme

Every project is different, so consider which of these sections apply to yours. The sections used in the template are suggestions for most open source projects. Also keep in mind that while a README can be too long and detailed, too long is better than too short. If you think your README is too long, consider utilizing another form of documentation rather than cutting out information.

## Name
Choose a self-explaining name for your project.

## Description
Let people know what your project can do specifically. Provide context and add a link to any reference visitors might be unfamiliar with. A list of Features or a Background subsection can also be added here. If there are alternatives to your project, this is a good place to list differentiating factors.

## Badges
On some READMEs, you may see small images that convey metadata, such as whether or not all the tests are passing for the project. You can use Shields to add some to your README. Many services also have instructions for adding a badge.

## Visuals
Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like ttygif can help, but check out Asciinema for a more sophisticated method.

## Installation
Within a particular ecosystem, there may be a common way of installing things, such as using Yarn, NuGet, or Homebrew. However, consider the possibility that whoever is reading your README is a novice and would like more guidance. Listing specific steps helps remove ambiguity and gets people to using your project as quickly as possible. If it only runs in a specific context like a particular programming language version or operating system or has dependencies that have to be installed manually, also add a Requirements subsection.

## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
If your project is open source, it's important to include a license. You can use this [website](https://choosealicense.com/) to help you pick one.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.

## Changelog
Make a README is inspired by Keep a Changelog. A changelog is another file that is very useful for programming projects.

## More Documentation
A README is a crucial but basic way of documenting your project. While every project should at least have a README, more involved ones can also benefit from a wiki or a dedicated documentation website. GitHub, Bitbucket, and GitLab all support maintaining a wiki alongside your project, and here are some tools and services that can help you generate a documentation website:

Daux.io
Docusaurus
GitBook
MkDocs
Read the Docs
ReadMe
Slate
Docsify

## Contributing
Just having a "Contributing" section in your README is a good start. Another approach is to split off your guidelines into their own file (CONTRIBUTING.md). If you use GitHub and have this file, then anyone who creates an issue or opens a pull request will get a link to it.

You can also create an issue template and a pull request template. These files give your users and collaborators templates to fill in with the information that you'll need to properly respond. This helps to avoid situations like getting very vague issues. Both GitHub and GitLab will use the templates automatically.