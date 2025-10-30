console.log("BS ECE 1-4 demo");
function countdown(num){
    console.log(num);
    if (num > 0) {
      setTimeout(() => countdown(num - 1), 1000);
    }
}
countdown(10);