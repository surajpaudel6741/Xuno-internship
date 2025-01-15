let a = 516;
let array = [];
let b = true;
while (b) {
  if (a % 2 == 0){
    a = a/2;
    array.push(a);
  }
  else {
    a = a * 3 + 1;
    array.push(a);
  }
  console.log(array.toString())
  if (array.length===4){
    if(array[1]===4 && array[2]=== 2) b = false;
    else array = [];
  }
}
console.log(a);
