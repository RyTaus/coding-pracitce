/*
  Problem found in CtCI.

  stringContainsPerm takes in 2 strings and returns all permutations of the first
  found in continuous characters of the second.
*/

const isPerm = (test, string) => {
  if (test.length !== string.length) {
    return false
  }
  if (test === '' && string === '') {
    return true;
  }
  if (string.includes(test[0])) {
    return isPerm(test.substring(1), string.replace(test[0], ''))
  }
  return false;
}

const stringContainsPerm = (small, large) => {
  let potentialAnswers = []
  const solutions = []
  for (let i = 0; i < large.length; i ++) {
    currLetter = large[i];
    potentialAnswers.push('')
    potentialAnswers = potentialAnswers.map(s => `${s}${large[i]}`)
    if (i >= small.length - 1) {
      const potentialSolution = potentialAnswers.shift()
      if (isPerm(potentialSolution, small)) {
        solutions.push(i - (small.length - 1));
      }
    }
  }

  return solutions;
}
