from inspect import cleandoc


def test_reformat_references():
    from deep_researcher.agents.long_writer_agent import reformat_references
    # Test Case 1: First section, no existing references
    draft = cleandoc("""# Research Report

    ## Table of Contents

    1. Introduction
    2. Market Analysis
    3. Competitive Landscape
    4. Conclusion

    """)
    section_markdown_1 = cleandoc(
    """## Introduction

    This report examines the technology landscape in 2023 [1](https://tech-trends.com/2023). 
    The rapid advancement of AI has been a major trend [2](https://ai-report.org/trends).
    Cloud computing continues to evolve with new paradigms [3](https://cloud-computing.org/evolution).
    """
    )
    references_1 = [
        "[1] https://tech-trends.com/2023",
        "[2] https://ai-report.org/trends",
        "[3] https://cloud-computing.org/evolution"
    ]

    section_markdown_2 = cleandoc(
    """## Market Analysis

    The global tech market is expected to reach $5 trillion by 2025 [1](https://market-research.com/tech-forecast).
    AI technologies, as mentioned earlier [2](https://ai-report.org/trends), are driving significant growth.
    Open source software is gaining prominence [3](https://opensource-trends.org/report).
    Cloud providers are seeing 30% year-over-year growth [4](https://cloud-computing.org/evolution).
    """
    )
    references_2 = [
        "[1] https://market-research.com/tech-forecast",
        "[2] https://ai-report.org/trends",
        "[3] https://opensource-trends.org/report",
        "[4] https://cloud-computing.org/evolution"
    ]
    
    section_markdown_3 = cleandoc(
    """## Competitive Landscape

    Major players in the tech industry include established giants [1](https://tech-giants.com/report) and emerging startups.
    New AI models [2](https://ai-report.org/trends) are disrupting traditional software development.
    The open source ecosystem [3](https://opensource-trends.org/report) creates a collaborative environment.
    Venture capital investment reached $150 billion in 2022 [4](https://vc-funding.org/tech-2022).
    Cloud market share is dominated by three major providers [5](https://cloud-computing.org/evolution).
    """
    )
    references_3 = [
        "[1] https://tech-giants.com/report",
        "[2] https://ai-report.org/trends",
        "[3] https://opensource-trends.org/report",
        "[4] https://vc-funding.org/tech-2022",
        "[5] https://cloud-computing.org/evolution"
    ]
    
    # Process each section in sequence
    all_references = []

    # Process the first section
    section_markdown_1, all_references = reformat_references(section_markdown_1, references_1, all_references)
    draft += section_markdown_1 + "\n\n"
    
    # Process the second section
    section_markdown_2, all_references = reformat_references(section_markdown_2, references_2, all_references)
    draft += section_markdown_2 + "\n\n"
    
    # Process the third section
    section_markdown_3, all_references = reformat_references(section_markdown_3, references_3, all_references)
    draft += section_markdown_3 + "\n\n"

    # Produce the final report
    final_report = draft + "## References:\n\n" + "\n".join(all_references)

    expected_final_report = cleandoc(
        """# Research Report

        ## Table of Contents

        1. Introduction
        2. Market Analysis
        3. Competitive Landscape
        4. Conclusion## Introduction

        This report examines the technology landscape in 2023 [1](https://tech-trends.com/2023). 
        The rapid advancement of AI has been a major trend [2](https://ai-report.org/trends).
        Cloud computing continues to evolve with new paradigms [3](https://cloud-computing.org/evolution).

        ## Market Analysis

        The global tech market is expected to reach $5 trillion by 2025 [4](https://market-research.com/tech-forecast).
        AI technologies, as mentioned earlier [2](https://ai-report.org/trends), are driving significant growth.
        Open source software is gaining prominence [5](https://opensource-trends.org/report).
        Cloud providers are seeing 30% year-over-year growth [3](https://cloud-computing.org/evolution).

        ## Competitive Landscape

        Major players in the tech industry include established giants [6](https://tech-giants.com/report) and emerging startups.
        New AI models [2](https://ai-report.org/trends) are disrupting traditional software development.
        The open source ecosystem [5](https://opensource-trends.org/report) creates a collaborative environment.
        Venture capital investment reached $150 billion in 2022 [7](https://vc-funding.org/tech-2022).
        Cloud market share is dominated by three major providers [3](https://cloud-computing.org/evolution).

        ## References:

        [1] https://tech-trends.com/2023
        [2] https://ai-report.org/trends
        [3] https://cloud-computing.org/evolution
        [4] https://market-research.com/tech-forecast
        [5] https://opensource-trends.org/report
        [6] https://tech-giants.com/report
        [7] https://vc-funding.org/tech-2022
        """
    )

    assert final_report == expected_final_report
