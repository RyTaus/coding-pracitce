/*
  This program is a currying function that chains together strings inputed in a
  currying fashion, and only returns the built string upon a call with an empty
  param. This is a question for one of LMU's junior classes that I decided to golf
  after helping a student.

  ex: say('hello')('world!')()
      returns 'hello world!'

  Character Count: 27
*/
s=(a='')=>b=>b?s(a+' '+b):a
