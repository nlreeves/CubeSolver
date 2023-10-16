const list = ['yellow','green','blue','red','orange','white'];

function* tabGen(tab) {
  let i = 0;
  let max = tab.length;

  while (true) {
    yield tab[i++];
    i %= max;
  }
}
const onTab = tabGen( list )

function onc(id) {
    id.style = "background-color: " + onTab.next().value;
}