
function change()
{
    xmlhttp= new XMLHttpRequest();
    xmlhttp.onreadystatechange=function()
    {
        document.getElementById("data").innerHTML="";                                                

        if(xmlhttp.readyState==4 && xmlhttp.status==200)
          {
            var x=JSON.parse(xmlhttp.responseText);
            var table=document.getElementById("mytable")
            for(var obj in x)
            {
                var row=table.insertRow();
                var cell1=row.insertCell();
                var cell2=row.insertCell();
                var cell3=row.insertCell();
                var cell4=row.insertCell();
                var cell5=row.insertCell();
                var cell6=row.insertCell();

                cell1.innerHTML+=x[obj].id;
                cell2.innerHTML+=x[obj].person;
                cell3.innerHTML+=x[obj].place;
                cell4.innerHTML+=x[obj].phone;
                cell5.innerHTML+=x[obj].email;
               
                
                var btn=document.createElement("button");
                btn.setAttribute("onclick","todo(this.id)");
                btn.setAttribute("id",x[obj].id);
                btn.innerHTML="Delete";
                cell6.appendChild(btn);

                var space=document.createTextNode("  ");
                cell6.appendChild(space);

                var btn=document.createElement("button");
                btn.setAttribute("id",x[obj].id);
                btn.setAttribute("name",obj);
                btn.setAttribute("onclick","update(this.id,this.name)");
                btn.innerHTML="Update";
                cell6.appendChild(btn);

            }
        }
    }
    xmlhttp.open("GET","http://127.0.0.1:8000/api/v1/detailed/",true);
    xmlhttp.send();
}

function todo(id)
{
    location.reload();
    Delete(id);
}



function update(id,name)
{
    alert("Allow to update the values of id  "+id);   
    var table=document.getElementById("mytable");
    var row=table.insertRow(parseInt(name)+2);
    var cell1=row.insertCell();
    var cell2=row.insertCell();
    var cell3=row.insertCell();
    var cell4=row.insertCell();
    var cell5=row.insertCell();
    var cell6=row.insertCell();

    cell1.innerHTML=id;
    cell1.setAttribute("id","id1");
    var input = document.createElement("input");
    input.setAttribute("id","name1");
    cell2.append(input);
    
    var input = document.createElement("input");
    input.setAttribute("id","place1");
    cell3.append(input);
    
    var input = document.createElement("input");
    input.setAttribute("id","phone1");
    cell4.append(input);


    var input = document.createElement("input");
    input.setAttribute("id","email1");
    cell5.append(input);


    var btn1 = document.createElement("button");
    btn1.innerHTML="Submit";
    btn1.setAttribute('onclick',"put('id1','name1','place1','phone1','email1')");
    cell6.appendChild(btn1);

    var space=document.createTextNode(" ");
    cell6.appendChild(space);


    var btn2=document.createElement("button");
    btn2.innerHTML="Cancel";
    btn2.setAttribute('onclick','cancel()');
    cell6.appendChild(btn2);
}

function cancel()
{
    location.reload();
}

function put(id,name,place,phone,email)
{
    var getid=document.getElementById(id).innerHTML;
    var getname = document.getElementById(name).value;
    var getplace = document.getElementById(place).value;
    var getphone = document.getElementById(phone).value;
    var getemail = document.getElementById(email).value;

    xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange=function()
    {
        document.getElementById("updating").innerHTML=xmlhttp.reponseText;
    }

    var updatedata= {
    "id": getid,
    "person": getname,
    "place": getplace,
    'phone':getphone,
    'email':getemail,
    }

    xmlhttp.open("PUT","http://127.0.0.1:8000/api/v1/Moredetail/"+getid+"/",true);
    xmlhttp.setRequestHeader("Content-type","application/json");
    xmlhttp.setRequestHeader("X-CSRFToken", '{{ csrf_token }}');
    console.log(JSON.stringify(updatedata));
    xmlhttp.send(JSON.stringify(updatedata));
    location.reload();
  

}


function Delete(id)
{
    alert("the data of  " +id+"  id is deleting");
    xmlhttp=new XMLHttpRequest();
    xmlhttp.onreadystatechange=function()
    {
        document.getElementById("mydelete").innerHTML=xmlhttp.reponseText;
    }
    xmlhttp.open("DELETE","http://127.0.0.1:8000/api/v1/Moredetail/"+id+"/",true);
    xmlhttp.send();
    
}

