#!/usr/bin/node
const callMeMoby = require('./101-call_me_moby').callMeMoby;
callMeMoby(3, function callMeMoby() {
  console.log('C is fun');
});
