{ bloque inicial }

let entero = "0|([1-9][0-9]*)"
let decimal = "([0-9]+\\.[0-9]*)|([0-9]*\\.[0-9]+)"
let hexadecimal = "0x[0-9A-Fa-f]+"
let operador_aritmetico = "\\+|\\-|\\*|\\/|\\%"
let potenciacion = "\\^"

rule tokens =
	entero               {print("Entero\n") }
  | decimal             {print("Decimal\n") }
  | hexadecimal         {print("Hexadecimal\n") }
  | operador_aritmetico {print("Operador aritmético\n") }
  | potenciacion        {print("Operador de potenciación\n") }