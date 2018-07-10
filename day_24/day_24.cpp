/**
 * day_24.cpp
 *
 * By Sebastian Raaphorst, 2018.
 */

#include <algorithm>
#include <fstream>
#include <iostream>
#include <vector>
#include <tuple>
#include <functional>

using Piece = std::pair<int,int>;
using Pieces = std::vector<Piece>;

class Bridge {
public:
    Bridge(const Pieces &p);

private:
    Pieces pieces;
};

Bridge::Bridge(const Pieces &p): pieces{p} {

}

/**
 * Recursive method to determine the greatest rank (by some chacteristc)  of a bridge using the specified pieces,
 * with the last connection being connector.
 * @param connector the connector end of the previous piece (0 to start)
 * @param pieces the pieces left
 * #param selected the pieces selected
 * @param rank so far
 * @param length so far
 * @return the highest score possible using these pieces
 */
int max_strength(int connector, Pieces pieces, int score) {
    // If we have no pieces left, we are done.
    if (pieces.empty())
        return score;

    // Find the candidate pieces for this position.
    std::vector<int> candidates;
    for (int i=0; i < pieces.size(); ++i) {
        const auto [a,b] = pieces[i];
        if (a == connector || b == connector)
            candidates.emplace_back(i);
    }
    if (candidates.empty())
        return score;

    int maxScore = score;
    for (const auto candidate: candidates) {
        const auto &piece = pieces[candidate];
        const auto [a, b] = piece;
        int nextConnector = connector == a ? b : a;


        Pieces remainingPieces = pieces;
        remainingPieces.erase(remainingPieces.begin() + candidate);

        int nextScore = max_strength(nextConnector, remainingPieces, score + a + b);
        if (nextScore > maxScore)
            maxScore = nextScore;
    }

    return maxScore;
}


int main() {
    Pieces pieces;

    std::ifstream pin("pieces.txt");
    int a, b;
    char d;
    while (pin >> a >> d >> b && d == '/') {
        pieces.emplace_back(std::make_pair(a, b));
    }

    int max_str =  max_strength(0, pieces, 0);
    std::cout << "Max strength is " << max_str << std::endl;
}
