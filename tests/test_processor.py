from pyarchunit import ArchitectureRule

def test_layers_respect_boundaries():
    rule = (
        ArchitectureRule()
        .modules_should_not_depend_on(['src.processor'], ['src.utils'])
        .because("el processor no debe llamar directamente a utils")
    )
    rule.check()

def test_no_circular_dependencies():
    rule = ArchitectureRule().modules_should_be_free_of_cycles()
    rule.check()
