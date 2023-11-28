# Run inside Juypter notebook cell. Example use:
# %run show_solutions.py W1_ex3
# Shows a button to toggle solutions tagged with 'W1_ex3'
# in the solutions script 'W1_solutions.txt'.

def toggle_solutions(question):
    # Import display functions
    import ipywidgets as widgets
    from IPython.display import display, Code, Markdown
    
    week = question.split('_')[0]
    
    #display(question.split('_'))
    
    #display(week)

    # Create button
    bt = widgets.Button(description='Reveal solution')

    # Create output area for the solution
    sol_area = widgets.Output(layout={'border': '1px solid green'})
    
    #open(f'{week}_solutions.txt', 'r')
    
    try:
        # Retrieve solution code from script, as a string
        with open(f'{week}_solutions.txt', 'r') as f:
            sol = []
            sol_block = ''
            out_format = []
            write_line = False

            # Read line-by-line
            for l in f:
                if l.startswith(f'###{question}_start'):
                    # Found starting tag, get format
                    out_format.append(l.strip().split('_')[-1])

                    # Start writing at the next line
                    write_line = True
                    continue

                # Continue writing lines until end tag
                if write_line:
                    if l.startswith(f'###{question}_end'):
                        # Reached the end tag, stop reading file
                        write_line = False
                        sol.append(sol_block)
                        break
                    elif l.startswith(f'###{question}_switch'):
                        # Switching output format for the next lines
                        out_format.append(l.strip().split('_')[-1])
                        sol.append(sol_block)
                        sol_block = ''
                        continue
                    else:
                        # Write line to current block
                        sol_block += l
                        
    except FileNotFoundError:
        sol = 'Solutions not yet released!'
        out_format = {}

    # Define how to display/hide the solution
    def toggle_answer(question):
        if bt.description == 'Reveal solution':
            # Display solution and change button label
            with sol_area:
                if not out_format:
                    print(sol)
                else:
                    for sol_block, fmt in zip(sol, out_format):
                        if fmt == 'py':
                            display(Code(data=sol_block, language='py'))
                        elif fmt == 'md':
                            display(Markdown(data=sol_block))
                        else:
                            print('Format not recognised...')
            bt.description = 'Hide solution'
        else:
            # Hide solution and change button label
            sol_area.clear_output()
            bt.description = 'Reveal solution'

    # When clicking the button, toggle solution
    bt.on_click(toggle_answer)

    # Show the button and the output area
    display(bt)
    display(sol_area)

if __name__ == "__main__":
    import sys
    
    # Create and display the widgets
    toggle_solutions(sys.argv[1])


