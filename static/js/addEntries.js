function calculateTotalTime() {
  let totalTime = 0;
  for (var i = 0; i < nrItemsLoaded; ++i) {
    if (itemsSelect[i] === 1) {
      totalTime += runtimes[i]
    } 
  }
  return totalTime;
}