
def is_criticality_balanced(temperature: int | float, neutrons_emitted: int | float) -> bool:
    
    return (temperature < 800) and (neutrons_emitted > 500) and (temperature * neutrons_emitted < 500000)

def reactor_efficiency(voltage: int | float, current: int | float, theoretical_max_power: int | float) -> str:
    
    power = voltage * current / theoretical_max_power * 100
    colors = ((80, 'green'), (60, 'orange'), (30, 'red'), (0, 'black'))
    
    return [color for output, color in colors if power >= output][0]

def fail_safe(temperature: int | float, neutrons_produced_per_second: int | float, threshold: int | float) -> str:
    
    if temperature * neutrons_produced_per_second < 0.9 * threshold:
        return 'LOW'
    elif 1.1 * threshold > temperature * neutrons_produced_per_second > 0.9 * threshold:
        return 'NORMAL'
    else:
        return 'DANGER'
