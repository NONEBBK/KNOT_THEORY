# volume_analyzer.py

import snappy
from knot_toolkit import Knot, calculate_hyperbolic_volume

if __name__ == '__main__':
    print("--- Starting Large-Scale Hyperbolic Volume Analysis ---")

    # SnapPy provides a built-in iterator for the knot census.
    # We will analyze all knots up to 11 crossings.
    max_crossings = 11
    knot_iterator = snappy.HTLinkExteriors(crossings=max_crossings)

    results = {}
    hyperbolic_knots_count = 0

    print(f"Calculating volumes for all knots up to {max_crossings} crossings...")

    for manifold in knot_iterator:
        # The iterator gives us manifold objects directly.
        # The name is available as an attribute.
        knot_name = manifold.name()

        # We can use our existing Knot class, passing the name.
        k = Knot(knot_name)
        volume = calculate_hyperbolic_volume(k)
        
        results[knot_name] = volume
        if volume > 0:
            hyperbolic_knots_count += 1

    print("\n--- Analysis Complete ---")

    # Filter out the non-hyperbolic knots for volume analysis
    hyperbolic_volumes = {name: vol for name, vol in results.items() if vol > 0}

    if hyperbolic_volumes:
        # Find the knot with the smallest and largest volume
        min_volume_knot = min(hyperbolic_volumes, key=hyperbolic_volumes.get)
        max_volume_knot = max(hyperbolic_volumes, key=hyperbolic_volumes.get)

        min_vol = hyperbolic_volumes[min_volume_knot]
        max_vol = hyperbolic_volumes[max_volume_knot]

        print(f"Total knots analyzed: {len(results)}")
        print(f"Number of hyperbolic knots found: {hyperbolic_knots_count}")
        print(f"Smallest non-zero volume: {min_vol:.6f} (Knot: {min_volume_knot})")
        print(f"Largest volume found: {max_vol:.6f} (Knot: {max_volume_knot})")
    else:
        print("No hyperbolic knots were found in the specified range.")
