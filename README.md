# Nikoo Book Club


Any summarizations or answers made with this code come with no warranty (see MIT license) and should not be used for financial, medical, legal, or any other critical applications.


### Set Up
   * Install Python3 from  https://www.python.org/downloads/

#### Virtual env 
   * Create virtual env 
     * python3 -m venv venv
   * Activate the source
     * source venv/bin/activate
   * Install the dependencies
     * pip3 install -r requirements.txt
     
#### Pycharm set up
   * Open the project in pycharm
   * Change Python interpreter to your venv path
       * Pycharm -> Preferences -> Python Interpreter 
       * Change Python Interpreter to <project_root>/venv/bin/python
    
### Deploy in Heroku
  * Login to Heroku 
     * Heroku login
  * Create an app
     * heroku create sf-vto-dev-tutorial
  * If app is already created then attach your git repo 
     * heroku git:remote sf-vto-dev-tutorial
  * deploy an app 
     * git push heroku master# nikoobookclub
