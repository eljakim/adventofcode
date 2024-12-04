fun main() {
    val regexp = Regex("(mul\\([0-9]+,[0-9]+\\))")
    val input = generateSequence(::readLine).joinToString("\n")
    val result = regexp.findAll(input)
    var s = 0
    for (r in result) {
        val ins = r.groups[0]!!.value.split(",")
        val a = ins[0].filter { it.isDigit() }.toInt()
        val b = ins[1].filter { it.isDigit() }.toInt()
        s += a * b
    }
    print(s)
}
