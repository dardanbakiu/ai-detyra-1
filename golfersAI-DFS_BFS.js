var players = 32;
var groupSize = 4;
var [javet, algoritmi] = weekConditions();

function ranNumber(num) {
  return num < 10 ? `${num} ` : `${num}`;
}

function getWeeks(weeks, players, groupSize) {
  for (const week of weeks) {
    const groups = [];
    for (let i = 0; i < players; i += groupSize)
      groups.push(
        week
          .filter((x, index) => index >= i && index < i + groupSize)
          .map((x) => ranNumber(x))
          .join(' ')
          .concat(' | ')
      );
    console.log(groups.join(' '));
  }
}

function weekConditions() {
  const n = 1;

  let algoritmi = process.argv[2];
  if (algoritmi !== 'dfs' && algoritmi !== 'bfs') {
    console.log('Algoritmi i gabuar');
    process.exit();
  }
  return [n, algoritmi];
}

function playersPerGroups(row, column, groupSize, weeks) {
  const group = Math.floor(column / groupSize);
  const groupStart = group * groupSize;
  const groupEnd = groupStart + groupSize - 1;
  return weeks[row].filter((x, index) => index >= groupStart && index <= groupEnd && x !== 0);
}

function delay(seconds) {
  const waitTill = new Date(new Date().getTime() + seconds * 1000);
  while (waitTill > new Date()) { }
}

function fillTab() {
  const firstTable = new Array(javet).fill().map((x) => new Array(players).fill(0));
  const tablesToVisit = [firstTable];
  const visitedTables = new Map();
  while (true) {
    if (!tablesToVisit.length) {
      console.log('No solution found');
      return;
    }

    let currentTable = algoritmi === 'dfs' ? tablesToVisit.pop() : tablesToVisit.shift();
    if (isSolution(currentTable)) {
      console.clear();
      getWeeks(currentTable, players, groupSize);
      return;
    }

    const hash = calculateTableHash(currentTable);
    if (!visitedTables.has(hash)) visitedTables.set(hash, []);

    visitedTables.get(hash).push(currentTable);

    const newTables = generateChildrenTables(currentTable);

    for (const table of newTables) {
      if (!tableExistsInArray(table, tablesToVisit) || !tableExistsInArray(table, visitedTables))
        tablesToVisit.push(table);
    }
  }
}

function isSolution(table) {
  const games = new Map();
  for (let i = 0; i < players; i++) {
    for (let j = 0; j < javet; j++) {
      const value = table[j][i];
      if (value === 0) return false;

      if (!games.has(value)) games.set(value, new Set());

      const otherGolfersInGroup = playersPerGroups(j, i, groupSize, table).filter(
        (x) => x === value
      );
      const alreadyPlayed = games.get(value);
      for (const golfer in otherGolfersInGroup) {
        if (alreadyPlayed.has(golfer)) return false;
        alreadyPlayed.add(golfer);
      }
    }
  }

  return true;
}

function generateChildrenTables(table) {
  let [rowOfEmptyCell, columnOfEmptyCell] = [0, 0];
  for (let i = 0; i < players; i++)
    for (let j = 0; j < javet; j++)
      if (table[j][i] === 0) {
        [rowOfEmptyCell, columnOfEmptyCell] = [j, i];
        return new Array(players).fill().map((x, index) => {
          x = JSON.parse(JSON.stringify(table));
          x[rowOfEmptyCell][columnOfEmptyCell] = index + 1;
          return x;
        });
      }

  return [];
}

function tableExistsInArray(table, arrayOfTables) {
  if (arrayOfTables instanceof Map) {
    const hash = calculateTableHash(table);
    if (!arrayOfTables.has(hash)) return false;

    for (const otherTable of arrayOfTables.get(hash))
      if (areTablesEqual(table, otherTable)) return true;

    return false;
  }

  for (const otherTable of arrayOfTables) if (areTablesEqual(table, otherTable)) return true;

  return false;
}

function calculateTableHash(table) {
  let sum = 0;
  table.forEach((x, i) => x.forEach((y, j) => (sum += y * (i + 100) + j)));
  return sum;
}

function areTablesEqual(table1, table2) {
  for (let i = 0; i < players; i++)
    for (let j = 0; j < javet; j++) if (table1[j][i] !== table2[j][i]) return false;

  return true;
}

fillTab();