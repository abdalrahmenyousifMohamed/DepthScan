from inspect import cleandoc


def test_reformat_section_headings():
    from deep_researcher.agents.long_writer_agent import reformat_section_headings

    # Test case 1: Empty input
    empty_input = ""
    assert reformat_section_headings(empty_input) == ""

    # Test case 2: Input with no headings
    no_headings = "This is just regular text\nwith multiple lines\nbut no headings"
    assert reformat_section_headings(no_headings) == no_headings

    # Test case 3: Input with h1 heading (should become h2)
    h1_input = "# Main Title\nSome content\n## Subtitle"
    expected_h1 = "## Main Title\nSome content\n### Subtitle"
    assert reformat_section_headings(h1_input) == expected_h1

    # Test case 4: Input with h3 heading (should become h2)
    h3_input = "### Deep Title\nSome content\n#### Subtitle"
    expected_h3 = "## Deep Title\nSome content\n### Subtitle"
    assert reformat_section_headings(h3_input) == expected_h3

    # Test case 5: Mixed heading levels
    mixed_input = cleandoc(
        """### Section
        Some content
        # Big Title
        More content
        #### Subsection
        """
    )
    expected_mixed = cleandoc(
        """## Section
        Some content
        # Big Title
        More content
        ### Subsection
        """
    )
    assert reformat_section_headings(mixed_input) == expected_mixed
