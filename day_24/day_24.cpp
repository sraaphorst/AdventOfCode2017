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
using MaximalChains = std::vector<Pieces>;


const MaximalChains findMaximalChains(int connector, const Pieces &piecesSoFar, Pieces pieces) {
    // Find the candidate pieces for this position.
    // If there are no pieces to end by we are done.
    std::vector<int> candidates;
    for (int i=0; i < pieces.size(); ++i) {
        const auto [a,b] = pieces[i];
        if (a == connector || b == connector)
            candidates.emplace_back(i);
    }
    if (candidates.empty()) {
        return MaximalChains{piecesSoFar};
    }

    MaximalChains chains;
    for (const auto candidate: candidates) {
        const auto piece = pieces[candidate];
        const auto [a, b] = piece;
        int nextConnector = connector == a ? b : a;

        Pieces remainingPieces = pieces;
        remainingPieces.erase(remainingPieces.begin() + candidate);

        Pieces newPiecesSoFar = piecesSoFar;
        newPiecesSoFar.emplace_back(piece);

        MaximalChains newChains = findMaximalChains(nextConnector, newPiecesSoFar, remainingPieces);
        std::copy(newChains.cbegin(), newChains.cend(), std::back_inserter(chains));
    }

    return chains;
}

const MaximalChains find_longest(const MaximalChains &chains) {
    MaximalChains maxchains;
    size_t len = 0;

    for  (const auto &c: chains) {
        if (c.size() < len) continue;
        if (c.size() > len) maxchains.clear();
        len = c.size();
        maxchains.emplace_back(c);
    }

    return maxchains;
}

int find_strongest(const MaximalChains &chains) {
    int strength = 0;

    for (const auto &c: chains) {
        int currStrength = 0;
        std::for_each(c.cbegin(), c.cend(), [&currStrength](const auto &p) {
            const auto [a,b]  = p;
            currStrength += a + b;
        });
        if (currStrength > strength)
            strength = currStrength;

    }

    return strength;
}

// Strongest is 1695
int main() {
    Pieces pieces;

    std::ifstream pin("pieces.txt");
    int a, b;
    char d;
    while (pin >> a >> d >> b && d == '/') {
        pieces.emplace_back(std::make_pair(a, b));
    }

    auto all = findMaximalChains(0, Pieces{}, pieces);
    auto max_str = find_strongest(all);
    std::cout << "*** Highest strength: " << max_str << std::endl;

    const auto mc  = find_longest(all);
    std::cout << "*** Maximum length highest strength is " << find_strongest(mc) << std::endl;
}
