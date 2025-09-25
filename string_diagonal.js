

function diagonalTraverse( inStr, numRows ){

  const resultBoard = Array(numRows).fill( []);
  for( let i = 0; i < numRows; i++ ){
    resultBoard[i] = Array(inStr.length).fill('');
  }
 // console.log(resultBoard);

  let row = 0;
  let col = 0;
  let count = 0;
  let directionDown = true;
  while( count < inStr.length ){
    resultBoard[row][col] = inStr[count];  
    if( row === 0 ) {
      directionDown = true;
    }

    if( row === numRows - 1 ){
      directionDown = false;
    }

    if( directionDown ){
      row++;
    } else {
      row--;
      col++
    }
    count++;    
  }

  //console.log(resultBoard);
  resultBoard.forEach( row => {
    console.log(row.map( cc => cc === "" ? " " : cc).join(''));
  })
  console.log("---------");

  const retStr = resultBoard.reduce( (acc, row) => acc += row.join(""), "");
  return retStr;
}

const testIt = ( testStr, rowNums ) => {
  console.log("Input: ", testStr, " rowNums: ", rowNums);
  console.log();
  console.log("Output: ", diagonalTraverse(testStr, rowNums));  
  console.log();
}

testIt( "INDEXINGIT", 3 );

testIt( "INDEXINGIT", 4 );


