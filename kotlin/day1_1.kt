import kotlin.math.abs

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

    var s = 0
    for (pair in left.zip(right)) {
        s += abs(pair.first - pair.second)
    }

    println(s)
}
