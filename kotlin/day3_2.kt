fun main() {
    val regexp = Regex("(mul\\([0-9]+,[0-9]+\\)|do\\(\\)|don't\\(\\))")
    val input = generateSequence(::readLine).joinToString("\n")
    val result = regexp.findAll(input)
    var s = 0
    var doing = true
    for (r in result) {
        val instruction = r.groups[0]!!.value
        when (instruction) {
            "do()" -> doing = true
            "don't()" -> doing = false
            else ->
                    if (doing) {
                        val ins = instruction.split(",")
                        val a = ins[0].filter { it.isDigit() }.toInt()
                        val b = ins[1].filter { it.isDigit() }.toInt()
                        s += a * b
                    }
        }
    }
    print(s)
}
