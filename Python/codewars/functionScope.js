function add(arg1){
  return function(arg2){
     return (arg1 + arg2);
  };
}


const add = a => b => a+b;


function curry(f) { // curry(f) выполняет каррирование
  return function(a) {
    return function(b) {
      return f(a, b);
    };
  };
}

// использование
function sum(a, b) {
  return a + b;
}

let add = curry(sum);
