package main

import (
  "fmt"
)

func main()  {
  var board [3][3]string = [3][3]string{{" "," "," "},
                                        {" "," "," "},
                                        {" "," "," "}}
  var player1 string = "X"
  var player2 string = "O"

  play(board,player1,player2);
}

func emptyCount(board [3][3]string) int{
  var count int = 0
  for i:=0; i<3; i++{
    for j:=0; j<3; j++{
      if board[i][j]==" "{
        count++
      }
    }
  }
  return count
}

func isWinner(board [3][3]string, player string) bool{
  //horizontal
  for i:=0; i<3; i++{
    if(board[i][0]==board[i][1] && board[i][1]==board[i][2] && board[i][0]==player){
      return true
    }
  }
  
  //vertical
  for i:=0; i<3; i++{
    if(board[0][i]==board[1][i] && board[1][i]==board[2][i] && board[0][i]==player){
      return true
    }
  }

  //diagonal
  if (board[0][0]==board[1][1] && board[1][1] ==board[2][2] && board[0][0]==player){
    return true;
  }

  if (board[0][2]==board[1][1] && board[1][1]==board[2][0] && board[0][2]==player){
    return true;
  }

  return false
}

func isDraw(board [3][3]string, p1 string, p2 string) bool{
  if !isWinner(board, p1) && ! isWinner(board, p2){
    if emptyCount(board) == 0{
      return true
    }
  }
  return false
}

func gameOver(board [3][3]string, p1 string, p2 string) bool{
  return isWinner(board,p1) || isWinner(board,p2) || isDraw(board,p1,p2)
}

func showBoard(board [3][3]string) {
  for i:=0;i<3; i++{
    fmt.Println(" --- --- --- ");
    fmt.Printf("| ");
    for j:=0; j<3; j++{
      fmt.Printf(board[i][j]+" | ");
    }
    fmt.Println();
  }
  fmt.Println(" --- --- --- ");
}

func play(board [3][3]string, p1 string, p2 string) {
  var player string = p1
  var n int
  for !gameOver(board,p1,p2){
    showBoard(board)
    fmt.Printf("> ")
    fmt.Scan(&n)

    if n>0 && n<10{
      n=n-1
      var r int = n/3
      var c int = n%3

      if board[r][c]==" "{
        board[r][c] = player
        if player==p1{
          player=p2
        }else{
          player=p1
        }

      }

    }
    fmt.Printf("\x1b[8A")
  }
  showBoard(board)

  if isWinner(board,p1){
    fmt.Println(p1,"Wins!")
  }else if isWinner(board,p2){
    fmt.Println(p2,"Wins!")
  }else{
    fmt.Println("Draw!")
  }

}

