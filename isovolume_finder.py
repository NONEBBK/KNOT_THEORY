# isovolume_finder.py

import snappy
from collections import defaultdict

def find_isovolume_knots(max_crossings=12):
    """
    Calculates hyperbolic volumes for a census of knots and identifies
    distinct knots that share the same volume.
    """
    print(f"--- Searching for Isovolumetric Knots up to {max_crossings} Crossings ---")
    
    precision = 8 
    volume_map = defaultdict(list)
    
    census_iterator = snappy.HTLinkExteriors(crossings=max_crossings)
    
    total_knots_processed = 0
    
    print("Processing knot census (this may take a few minutes)...")
    for manifold in census_iterator:
        # The correct method to check for single-component links (knots) is num_cusps().
        if manifold.num_cusps() != 1:
            continue
            
        total_knots_processed += 1
        
        try:
            volume = round(float(manifold.volume()), precision)
        except RuntimeError:
            volume = 0.0
            
        if volume > 0:
            volume_map[volume].append(manifold.name())

    print(f"\nAnalysis complete. Processed {total_knots_processed} knots.")
    
    isovolume_sets = {vol: names for vol, names in volume_map.items() if len(names) > 1}
    
    if not isovolume_sets:
        print("\nNo pairs of knots with identical volumes were found in this census.")
    else:
        print(f"\nSUCCESS: Found {len(isovolume_sets)} sets of knots with identical volumes:")
        for volume, names in isovolume_sets.items():
            print(f"  - Volume: {volume:.{precision}f} -> Knots: {', '.join(names)}")

if __name__ == '__main__':
    find_isovolume_knots(max_crossings=12)
