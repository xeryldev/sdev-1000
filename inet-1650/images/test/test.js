function something(xyz) {
  a = xyz.split("");
  z = '';
  for(i=a.length-1; i >= 0; i--) {
    z = z + a[i];
  }
  return z;
}
console.log(something('How are you?'));