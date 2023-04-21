{ bloque inicial }

let digito = "1|2|3"
let numero = "digito(digito)*"
let letra = "a|b|c"
let identificador = "letra(letra|digito)*"
let if = "if"
let else = "else"

rule tokens =
	digito            {print("Digito\n") }
  | numero 			    {print("Numero\n") }
  | letra			      {print("Letra\n") }
  | identificador	  {print("Identificador\n") }
  | if              {print("if\n")} 
  | else            {print("else\n")}

{ bloque final }
