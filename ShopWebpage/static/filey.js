
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

                cell1.innerHTML+=x[obj].id;
                cell2.innerHTML+=x[obj].name;
                cell3.innerHTML+=x[obj].item;
                cell4.innerHTML+=x[obj].time;

                
                var btn=document.createElement("button");
                btn.setAttribute("onclick","todo(this.id)");
                btn.setAttribute("id",x[obj].id);
                btn.innerHTML="Delete";
                cell5.appendChild(btn);

                               
                 var space=document.createTextNode("  ");
                 cell5.appendChild(space);



                var btn=document.createElement("button");
                btn.setAttribute("id",x[obj].id);
                btn.setAttribute("name",obj);
                btn.setAttribute("onclick","update(this.id,this.name)");
                btn.innerHTML="Update";
                cell5.appendChild(btn);

            }
        }
    }
    xmlhttp.open("GET","http://127.0.0.1:8000/api/v1/orderdetailed/",true);
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
    cell1.innerHTML=id;
    cell1.setAttribute("id","id1");
    var input = document.createElement("input");
    input.setAttribute("id","name1");
    cell2.append(input);
    var input = document.createElement("input");
    input.setAttribute("id","item1");
    cell3.append(input);
    var input = document.createElement("input");
    input.setAttribute("type","datetime-local");
    input.setAttribute("id","time1");
    cell4.append(input);
    var btn1 = document.createElement("button");
    btn1.innerHTML="Submit";
    btn1.setAttribute('onclick',"put('id1','name1','item1','time1')");
    cell5.appendChild(btn1);

    var space=document.createTextNode(" ");
    cell5.appendChild(space);

    var btn2=document.createElement("button");
    btn2.innerHTML="Cancel";
    btn2.setAttribute("onclick","cancel("+name+")");
    cell5.appendChild(btn2);

}

function cancel(name)
{
    document.getElementById("mytable").deleteRow(parseInt(name)+2);
}

function put(id,name,item,time)
{
    var getid=document.getElementById(id).innerHTML;
    var getname = document.getElementById(name).value;
    var getitem = document.getElementById(item).value;
    var gettime = document.getElementById(time).value;

    xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange=function()
    {
        document.getElementById("updating").innerHTML=xmlhttp.reponseText;
    }

    var updatedata= {
    "id": getid,
    "name": getname,
    "item": getitem,
    "time": gettime
    }

    xmlhttp.open("PUT","http://127.0.0.1:8000/api/v1/orderMoredetail/"+getid+"/",true);
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
    xmlhttp.open("DELETE","http://127.0.0.1:8000/api/v1/orderMoredetail/"+id+"/",true);
    xmlhttp.send();
    
}


