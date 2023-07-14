// creating express frame work
const express = require('express')

// to access mysql making an mysql object/var
const { Pool } = require('pg');

// creating express app
const app = express()

// serivce port 
const port = 9010;

var cnt = 0;

// creating an object to connect to database 
const pool = new Pool({
  user: 'postgres',
  host: '172.19.13.100',
  database: 'group_10',
  password: 'test',
  port: 5432, // the default PostgreSQL port
});



app.use((req, res, next) => {
  console.log(req.body);
  
  res.setHeader('Access-Control-Allow-Origin', '*')
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type')
  next()
})


// This responds with "all data" on the homepage
app.get('/alldata', function (req, res) {
    cnt = cnt+1;
    pool.query('SELECT * FROM group_10_data', (error, results) => {
    	if (error) {
    		throw error;
    	}
    	res.send(results.rows);
    });
    
    console.log(cnt);

   
 })
 
 
 // respons with all the temprature 
 app.get('/temprature', function (req, res){
     
     pool.query('SELECT temp FROM group_10_data', (error, results) =>{
     	if(error){
     		throw error;
     	}
     	res.send(results.rows);
     });
     
 });
 
 
  // respons with all the humidity 
 app.get('/humidity', function (req, res){
     
     pool.query('SELECT humi FROM group_10_data limit 10', (error, results) =>{

     	if(error){
     		throw error;
     	}
     	res.send(results.rows);
     });
     	
     
 });
 
  // respons with all the humidity 
 app.get('/latest_date_time', function (req, res){
     var lim = 1
     var q = `select * from group_10_data order by date desc, time desc limit ${lim}`
     pool.query(q, (error, results) =>{

     	if(error){
     		throw error;
     	}
     	res.send(results.rows);
     });
     	
     
 });
 
   // respons with all the humidity 
 app.get('/range_query', function (req, res){
     var startDate = "2023-04-14";
     var startTime = "00:59:00";
     var endDate = "2023-04-14";
     var endTime = "01:00:00";
     var q = `SELECT * FROM group_10_data where date >= '%${startDate}%' AND time >= '%${startTime}%' AND date <= '%${endDate}%' AND time <= '%${endTime}%'`
     pool.query(q, (error, results) =>{

     	if(error){
     		throw error;
     	}
     	
     	
     	
     	res.send(results.rows);
     });
     	
     
 });
 
app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})

