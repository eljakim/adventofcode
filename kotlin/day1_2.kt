fun main() {
    val input = generateSequence(::readLine)
    val left = mutableListOf<Int>()
    val right = mutableListOf<Int>()

    for (line in input) {
        val ints = line.split("\\s+".toRegex()).map { it.toInt() }
        left.add(ints[0])
        right.add(ints[1])
    }
    left.sort()
    right.sort()

    val r = right.groupingBy { it }.eachCount()
    var s = 0
    for (l in left) {
        if (r.containsKey(l)) {
            s += l * r[l]!!
        }
    }
    print(s)
}
