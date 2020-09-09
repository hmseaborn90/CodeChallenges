function whichIsLarger(f, g) {
  return f() > g() ? "f" : g() > f() ? "g" : "neither";
}

function whichIsLarger(f, g) {
  const fval = f(),
    gval = g();
  return fval > gval ? "f" : gval > fval ? "g" : "neither";
}

function whichIsLarger(f, g) {
  const o = f();
  const t = g();
  if (o > t) {
    return "f";
  } else if (t > o) {
    return "g";
  } else {
    return "neither";
  }
}
