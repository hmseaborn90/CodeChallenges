function areThereDuplicates(...args) {
    // good luck. (supply any arguments you deem necessary.)
    let values = {};
    for (let i in args) {
      values[args[i]] = (values[args[i]] || 0) + 1;
    }
    for (let key in values) {
      if (values[key] > 1) return true;
    }
    return false;
  }
  


  function areThereDuplicates() {
      return new Set(arguments).size !== arguments.length;
  }