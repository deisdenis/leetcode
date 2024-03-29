# problem origin: https://leetcode.com/problems/most-common-word/
#
# Given a paragraph and a list of banned words, return the most frequent word that is not in the list of banned words.
# It is guaranteed there is at least one word that isn't banned, and that the answer is unique.
#
# Words in the list of banned words are given in lowercase, and free of punctuation. Words in the paragraph are not case
# sensitive.The answer is in lowercase.
#
# Example:
#   Input paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
#   banned = ["hit"]
#   Output: "ball"
#   Explanation: "hit" occurs 3 times, but it is a banned word. "ball" occurs twice( and no other word does), so it is
#   the most frequent non - banned word in the paragraph. Note that words in the paragraph are not case sensitive,
#   that punctuation is ignored(even if adjacent to words, such as "ball,"), and that "hit" isn 't the answer even
#   though it occurs more because it is banned.
#
# Note:
#   1 <= paragraph.length <= 1000.
#   0 <= banned.length <= 100.
#   1 <= banned[i].length <= 10.
#   The answer is unique, and written in lowercase(even if its occurrences in paragraph may have uppercase symbols,
#   and even if it is a proper noun.) paragraph only consists of letters, spaces, or the punctuation symbols !?',;.
#   There are no hyphens or hyphenated words. Words only consist of letters, never apostrophes or other punctuation
#   symbols.


class Solution:
    def mostCommonWord(self, paragraph: str, banned: list) -> str:
        # time O(n) -> n = size of paragraph + size of banned
        # space O(n)
        # clean string
        paragraph = paragraph.lower()
        paragraph = ' ' + paragraph + ' '
        for char in ['!', '?', ',', ';', '.', '\'']:
            paragraph = paragraph.replace(char, ' ')
        # string to array
        paragraph = paragraph.split()
        dict = {}
        mx = 0
        for word in paragraph:
            if word not in banned:
                if word in dict:
                    dict[word] += 1
                    if dict[word] > mx:
                        mx = dict[word]
                        leader = word
                else:
                    dict[word] = 1
                    if dict[word] > mx:
                        mx = dict[word]
                        leader = word
        return leader


test_list = [["Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]], ["a, a, a, a, b,b,b,c, c", ["a"]],
             ["abc abc? abcd the jeff!", ["abc", "abcd", "jeff"]],
             ["j. t? T. z! R, v, F' x! L; l! W. M; S. y? r! n; O. q; I? h; w. t; y; X? y, p. k! k, h, J, r? w! U! V; j' u; R! z. s. T' k. P? M' I' j! y. P, T! e; X. w? M! Y, X; G; d, X? S' F, K? V, r' v, v, D, w, K! S? Q! N. n. V. v. t? t' x! u. j; m; n! F, V' Y! h; c! V, v, X' X' t? n; N' r; x. W' P? W; p' q, S' X, J; R. x; z; z! G, U; m. P; o. P! Y; I, I' l' J? h; Q; s? U, q, x. J, T! o. z, N, L; u, w! u, S. Y! V; S? y' E! O; p' X, w. p' M, h! R; t? K? Y' z? T? w; u. q' R, q, T. R? I. R! t, X, s? u; z. u, Y, n' U; m; p? g' P? y' v, o? K? R. Q? I! c, X, x. r' u! m' y. t. W; x! K? B. v; m, k; k' x; Z! U! p. U? Q, t, u' E' n? S' w. y; W, x? r. p! Y? q, Y. t, Z' V, S. q; W. Z, z? x! k, I. n; x? z; V? s! g, U; E' m! Z? y' x? V! t, F. Z? Y' S! z, Y' T? x? v? o! l; d; G' L. L, Z? q. w' r? U! E, H. C, Q! O? w! s? w' D. R, Y? u. w, N. Z? h. M? o, B, g, Z! t! l, W? z, o? z, q! O? u, N; o' o? V; S! z; q! q. o, t! q! w! Z? Z? w, F? O' N' U' p? r' J' L; S. M; g' V. i, P, v, v, f; W? L, y! i' z; L? w. v, s! P?",
                ["m","q","e","l","c","i","z","j","g","t","w","v","h","p","d","b","a","r","x","n"]]]

answers = []

solution = Solution()
for test_value in test_list:
    answers.append(str(solution.mostCommonWord(test_value[0], test_value[1])))
assert answers == ["ball", "b", "the", "y"], str(answers) + ' is wrong solution'
print('Everything looks fine!')
