
var btn = document.querySelector('.add');
var remove = document.querySelector('.draggable');

function dragStart(e) {
  this.style.opacity = '0.4';
  dragSrcEl = this;
  e.dataTransfer.effectAllowed = 'move';
  e.dataTransfer.setData('text/html', this.innerHTML);
};

function dragEnter(e) {
  this.classList.add('over');
}

function dragLeave(e) {
  e.stopPropagation();
  this.classList.remove('over');
}

function dragOver(e) {
  e.preventDefault();
  e.dataTransfer.dropEffect = 'move';
  return false;
}

function dragDrop(e) {
  if (dragSrcEl != this) {
    dragSrcEl.innerHTML = this.innerHTML;
    this.innerHTML = e.dataTransfer.getData('text/html');
  }
  return false;
}

function dragEnd(e) {
  var listItens = document.querySelectorAll('.draggable');
  [].forEach.call(listItens, function (item) {
    item.classList.remove('over');
  });
  this.style.opacity = '1';
}

function addEventsDragAndDrop(el) {
  el.addEventListener('dragstart', dragStart, false);
  el.addEventListener('dragenter', dragEnter, false);
  el.addEventListener('dragover', dragOver, false);
  el.addEventListener('dragleave', dragLeave, false);
  el.addEventListener('drop', dragDrop, false);
  el.addEventListener('dragend', dragEnd, false);
}

var listItens = document.querySelectorAll('.draggable');
[].forEach.call(listItens, function (item) {
  addEventsDragAndDrop(item);
});


function change() {
  var x = document.createElement("P");
  x.innerHTML = document.getElementById("space").value;
  x.onclick = () => { myFunction(x) };
  var items = document.getElementById('text');
  items.appendChild(x);
  document.getElementById("space").value = "";
}
function change2(element) {
  
  document.getElementById("do").innerHTML = "<input id=in> ";
  
  var inputElement = document.createElement('input');
  inputElement.type = "button"
  document.getElementById("do").append(inputElement);
  inputElement.addEventListener('click', function(){
    change1(element);
});
}

function change1(element) {
  debugger;
  element.innerHTML = document.getElementById("in").value;
}

function myFunction(element) {
  element.classList.toggle("dark");
}

let i = 0;
let j = 0;
function addNewItem() {
  
  var newItem = document.querySelector('.input').value;
  if (newItem != '') {
    document.querySelector('.input').value = '';
    var p = document.createElement("P");
    var attr = document.createAttribute('draggable');
    var div = document.querySelector('div');
    p.className = 'draggable';
    attr.value = 'true';
    p.setAttributeNode(attr);
    p.appendChild(document.createTextNode(newItem));
    p.onclick = () => { myFunction(p) };
    p.ondblclick = () => { change2(p) };
    div.appendChild(p);
    addEventsDragAndDrop(p);
    document.getElementsByTagName("P")[i].setAttribute("id", i);
    //document.getElementsByTagName("P")[i].setAttribute("ondblclick", "change2()");
    i = i + 1;

    var div1 = document.getElementById("text");
    //let p1 = div1.getElementsByTagName("p");
   // var docs = document.getElementById("collect");

    document.getElementById("collect").innerHTML += (document.getElementsByTagName("p")[j].id);

    j = j + 1;

    console.log('docs');
  }
}

