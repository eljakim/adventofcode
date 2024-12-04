fun main() {
    val input = generateSequence(::readLine)
    val levels = mutableListOf<List<Int>>()
    var safe = 0

    for (line in input) {
        val ints = line.split("\\s+".toRegex()).map { it.toInt() }
        levels.add(ints)
    }

    for (l in levels) {
        val diffs = l.zip(l.drop(1)).map { it.first - it.second }
        val max: Int = diffs.maxOrNull() ?: 0
        val min: Int = diffs.minOrNull() ?: 0
        if ((max in -3..-1) and (min >= -3)) {
            safe += 1
        }
        if ((min in 1..3) and (max <= 3)) {
            safe += 1
        }
    }

    println(safe)
}
