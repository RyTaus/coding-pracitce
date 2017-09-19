/*
  The curry function takes a function whose parameter is a list and turns it into
  a curryable function.
*/

const curry = (fun) => {
  const curr = (input, sofar = [], fun) => {
    if (input) {
      sofar.push(input);
      return (next) => {
        return curr(next, sofar, fun);
      }
    } else {
      return fun(sofar);
    }
  };

  return (next) => {
    return curr(next, [], fun);
  };
};

let add = (list) => {
  let sum = 0;
  for (n in list) {
	   sum += list[n];
  };
  return sum;
};

let curryAdd = curry(add);

console.log( curryAdd(4)(6)(7)() );
