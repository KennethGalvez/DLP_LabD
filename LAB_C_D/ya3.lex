{ bloque inicial }

let identificador = "[a-zA-Z][a-zA-Z0-9]*xyz"
let entero = "0|([1-9][0-9]*)"
let decimal = "([0-9]+\\.[0-9]*)|([0-9]*\\.[0-9]+)"
let cadena_caracteres = "\"[a-zA-Z0-9\\s]*\""
let operador_aritmetico = "\\+|\\-|\\*|\\/|\\%"
let operador_potenciacion = "\\^"

rule tokens =
	identificador          {print("Identificador\n") }
  | entero                 {print("Entero\n") }
  | decimal               {print("Decimal\n") }
  | "if"                  {print("if\n") }
  | "for"                 {print("for\n") }
  | cadena_caracteres     {print("Cadena de caracteres\n") }
  | operador_aritmetico   {print("Operador aritmético\n") }
  | operador_potenciacion {print("Operador de potenciación\n") }