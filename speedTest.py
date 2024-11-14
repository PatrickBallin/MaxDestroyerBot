import cProfile
import pstats

from Evaluation import evaluiere_schachbrett
from Evaluation import get_big_babba_move

figuren = {
    "w_ba": int("0000000000000000000000000000000000000000000000001111111100000000", 2),
    "w_la": int("0000000000000000000000000000000000000000000000000000000000100100", 2),
    "w_pf": int("0000000000000000000000000000000000000000000000000000000001000010", 2),
    "w_tu": int("0000000000000000000000000000000000000000000000000000000010000001", 2),
    "w_da": int("0000000000000000000000000000000000000000000000000000000000010000", 2),
    "w_ko": int("0000000000000000000000000000000000000000000000000000000000001000", 2),

    "s_ba": int("0000000011111111000000000000000000000000000000000000000000000000", 2),
    "s_la": int("0010010000000000000000000000000000000000000000000000000000000000", 2),
    "s_pf": int("0100001000000000000000000000000000000000000000000000000000000000", 2),
    "s_tu": int("1000000100000000000000000000000000000000000000000000000000000000", 2),
    "s_da": int("0001000000000000000000000000000000000000000000000000000000000000", 2),
    "s_ko": int("0000100000000000000000000000000000000000000000000000000000000000", 2)
}


def profile_evaluiere_schachbrett():
    get_big_babba_move(figuren, True, 4)


if __name__ == '__main__':
    # Profile the function
    profiler = cProfile.Profile()
    profiler.enable()

    profile_evaluiere_schachbrett()

    profiler.dump_stats('eval_profile.prof')
    profiler.disable()

    # Print the profiling stats
    stats = pstats.Stats(profiler)
    stats.strip_dirs().sort_stats('cumtime').print_stats(10)  # Print the top 10 functions

    # Optionally: Save the profiling data for further analysis
    # profiler.dump_stats('eval_profile.prof')
