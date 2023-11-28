# Lines 12-13 from users Alex and cqcn1991 on StackOverflow, July 2015 to April 2016.
# Published under CC BY-SA 3.0
# https://stackoverflow.com/a/31750982

# Lines 15-16 from user krishnab on StackOverflow, June 2018.
# Published under CC BY-SA 4.0
# https://stackoverflow.com/a/50921391

if __name__ == "__main__":

    from IPython.display import display, Javascript, HTML
    import sys

    try:
        # Run only if the solutions are released
        with open(f'{sys.argv[1]}_solutions.txt', 'r'):
            js = """<script type='text/javascript' src='scripts/create_widgets.js'></script>"""
            display(HTML(js))

            def runSolutionCells():
                display(Javascript("window.runSolutionCells()"))
            
            runSolutionCells()
            print('Buttons created!')
        
    except FileNotFoundError:
        print('Solutions not yet released!')

import sys
sys.argv
