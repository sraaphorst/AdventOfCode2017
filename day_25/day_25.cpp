/**
 * day_25.cpp
 *
 * By Sebastian Raaphorst, 2018.
 */

#include <algorithm>
#include <deque>
#include <iostream>

enum class State {
    A,
    B,
    C,
    D,
    E,
    F,
};

class TuringMachine {
public:
    TuringMachine();
    ~TuringMachine() = default;

    void transition() noexcept;

    int diagnostic_checksum() const noexcept;

private:
    std::deque<int> tape;
    State state;
    int headpos;

    int tape_size() const noexcept;
};

TuringMachine::TuringMachine()
        : state{State::A}, headpos{}, tape{0} {}

int TuringMachine::tape_size() const noexcept {
    return static_cast<int>(tape.size());
}

void TuringMachine::transition() noexcept {
    while (headpos >= tape_size()) {
        tape.emplace_back(0);
    }
    if (headpos < 0)
        while (headpos < 0) {
            tape.emplace_front(0);
            ++headpos;
        }

    switch (state) {
        case State::A:
            if (tape[headpos] == 0) {
                tape[headpos] = 1;
                ++headpos;
                state = State::B;
            } else {
                tape[headpos] = 0;
                --headpos;
                state = State::B;
            }
            break;

        case State::B:
            if (tape[headpos] == 0) {
                tape[headpos] = 0;
                ++headpos;
                state = State::C;
            } else {
                tape[headpos] = 1;
                --headpos;
                state = State::B;

            }
            break;

        case State::C:
            if (tape[headpos] == 0) {
                tape[headpos] = 1;
                ++headpos;
                state = State::D;
            } else {
                tape[headpos] = 0;
                --headpos;
                state = State::A;
            }
            break;

        case State::D:
            if (tape[headpos] == 0) {
                tape[headpos] = 1;
                --headpos;
                state = State::E;
            } else {
                tape[headpos]= 1;
                --headpos;
                state = State::F;
            }
            break;

        case State::E:
            if (tape[headpos] == 0) {
                tape[headpos] = 1;
                --headpos;
                state = State::A;
            } else {
                tape[headpos] = 0;
                --headpos;
                state = State::D;
            }
            break;

        case State::F:
            if (tape[headpos] == 0) {
                tape[headpos] = 1;
                ++headpos;
                state = State::A;
            } else {
                tape[headpos] = 1;
                --headpos;
                state = State::E;
            }
            break;
    }
}

int TuringMachine::diagnostic_checksum() const noexcept {
    return static_cast<int>(std::count(tape.cbegin(), tape.cend(), 1));
}

int main() {
    TuringMachine t;
    for (int i = 0; i < 12629077; ++i) {
        t.transition();
    }
    std::cout << t.diagnostic_checksum() << std::endl;
}
