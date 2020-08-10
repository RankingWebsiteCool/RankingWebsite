function showTotalRuntime() {
  M.Toast.dismissAll();
  setTimeout(() => {  M.toast({html: 'Total runtime : ' + calculateTotalTime(), displayLength: 5000}); }, 100);
}

function updateEntries(button) {
    button_type = button.name.charAt(0)
    if (button_type === 'e') {
            arrayInd = Number(button.name.substring(1));
            itemsSelect[arrayInd] = Number(button.checked);
    }
    showTotalRuntime();
}