
//var app=require('./function.js');

var http = require('http');
var fs = require('fs');
http.createServer(function (req, res) {
  fs.writeFile("testabc1", "app.docs", function(err) {
    if(err) {
        return console.log(err);
    }
    console.log("The file was saved!");
    res.end();
});
    
}).listen(8080);
