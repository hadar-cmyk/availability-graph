This repo is made to display interactive graph of availability that depends on two parameters lambda and mu, but as well as plotly allows to create one slider - constaints will depend on parameters named as hour.

So lambda = 1-10/hours

mu = 1/hours

Here is an initial link to graph [a link](http://availability-graph.herokuapp.com/)



# How to deploy your own heroku app

1. Fork that repository to make all necessary files available for deploying on heroku  ( push that button  `fork`) / or you could download repo using 

![IMG](https://i.imgur.com/MXxwxPV.png)



![IMG](https://i.imgur.com/bMkYjNP.png)


2. Login to Heroku (or if you don't have an account - register) and create new app 

![Heroku dashboard](https://miro.medium.com/max/1400/1*SmjIEaSRd6bCofGNG42YFw.png)

3. Select `github` as your deployment method, and then search for your repo (note that it will appear under your name, not mine, since you already forked it!). Go ahead and pick “connect”.

![Github method](https://miro.medium.com/max/1400/1*9DkMgBhoZzo_AaxM-NyoDg.png)

4. There will be 2 option how to deploy branches : manual or authomatic. Authomatic deployment method will track all commit in branch and in case of files will be changed - deployment authomaticaly displays on app link. In case of manual deploy - every changes should be deployed manualy on the next option of heroku dashboard 

![Manual](https://miro.medium.com/max/1400/1*ZC0lXi42U6vvSSTYK1wKew.png)
![Manual](https://miro.medium.com/max/1400/1*NLn1SLM_Ds8mEh7AqK5DgQ.png)

5. Your app is ready for operation, in my case it is available on next [link](http://availability-graph.herokuapp.com/)


---

[According to user's tutorial](https://austinlasseter.medium.com/how-to-deploy-a-simple-plotly-dash-app-to-heroku-622a2216eb73)
