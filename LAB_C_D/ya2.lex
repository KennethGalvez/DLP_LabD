{ bloque inicial }

let identificador = "[a-zA-Z][a-zA-Z0-9]*"
let entero = "0|([1-9][0-9]*)"
let operador_aritmetico = "\\+|\\-|\\*|\\/|\\%"

rule tokens =
	identificador      {print("Identificador\n") }
  | entero             {print("Entero\n") }
  | operador_aritmetico {print("Operador aritmético\n") }
  | "if"              {print("if\n") }
  | "for"             {print("for\n") }
  | "while"           {print("while\n") }
