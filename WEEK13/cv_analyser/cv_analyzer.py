import google.generativeai as genai
import PyPDF2
import os
import sys
from pathlib import Path
from typing import Optional, List, Dict
from abc import ABC, abstractmethod


class CVAnalyzer:
    """
    Professional CV Analyzer using Gemini AI with Object-Oriented Programming.
    
    This class encapsulates all CV analysis functionality including PDF processing,
    AI-powered analysis, and report generation.
    """
    
    def __init__(self, api_key: str, model_name: str = "gemini-1.5-pro-latest"):
        """
        Initialize the CV Analyzer with Gemini API configuration.
        
        Args:
            api_key (str): Google Gemini API key
            model_name (str): Gemini model to use for analysis
        """
        self.api_key = api_key
        self.model_name = model_name
        self.gemini_model = None
        self.quick_model = None
        self._configure_api()
    
    def _configure_api(self) -> None:
        """Configure Gemini API with the provided key."""
        try:
            genai.configure(api_key=self.api_key)
            self.gemini_model = genai.GenerativeModel("gemini-2.5-flash")
            self.quick_model = genai.GenerativeModel('gemini-2.5-flash')
            print("✅ Gemini API configured successfully")
        except Exception as e:
            raise Exception(f"Failed to configure Gemini API: {e}")


class PDFProcessor:
    """
    Handles PDF file operations including text extraction and file management.
    """
    
    @staticmethod
    def extract_text_from_pdf(pdf_path: Path) -> Optional[str]:
        """
        Extract text content from PDF file.
        
        Args:
            pdf_path (Path): Path to the PDF file
            
        Returns:
            Optional[str]: Extracted text or None if extraction fails
        """
        try:
            with open(pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text() + "\n"
            return text
        except Exception as e:
            print(f"Error reading PDF file: {e}")
            return None
    
    @staticmethod
    def find_pdf_files(directory: Path) -> List[Path]:
        """
        Find all PDF files in the specified directory.
        
        Args:
            directory (Path): Directory to search for PDF files
            
        Returns:
            List[Path]: List of PDF file paths
        """
        return list(directory.glob("*.pdf"))


class PromptEngineering:
    """
    Handles advanced prompt engineering for CV analysis.
    """
    
    @staticmethod
    def create_comprehensive_analysis_prompt(cv_text: str, target_role: Optional[str] = None, 
                                           industry: Optional[str] = None) -> str:
        """
        Create comprehensive analysis prompt using advanced prompt engineering.
        
        Args:
            cv_text (str): Extracted CV text
            target_role (Optional[str]): Target job role for analysis
            industry (Optional[str]): Target industry for analysis
            
        Returns:
            str: Engineered prompt for comprehensive analysis
        """
        return f"""
    You are a senior HR professional and career advisor with 15+ years of experience in recruitment and CV evaluation. 
    Analyze the following CV comprehensively and provide detailed feedback.

    CV CONTENT:
    {cv_text}

    ANALYSIS REQUIREMENTS:
    Please provide a thorough analysis covering these aspects:

    1. OVERALL ASSESSMENT (Score: 1-10)
       - Overall CV quality rating
       - First impression assessment
       - Professional presentation evaluation

    2. STRUCTURE & FORMATTING ANALYSIS
       - Layout and visual appeal
       - Section organization and flow  
       - Readability and clarity
       - Professional formatting consistency
       - Length appropriateness

    3. CONTENT EVALUATION
       a) Contact Information:
          - Completeness and professionalism
          - Missing essential details
       
       b) Professional Summary/Objective:
          - Clarity and impact
          - Relevance to career goals
          - Compelling value proposition
       
       c) Work Experience:
          - Relevance and progression
          - Achievement quantification
          - Action verb usage
          - Gap identification
          - Description quality
       
       d) Skills Section:
          - Technical skills relevance
          - Soft skills representation  
          - Skill categorization
          - Industry alignment
       
       e) Education:
          - Relevance to career path
          - Certifications and qualifications
          - Additional training/courses

    4. ATS COMPATIBILITY ASSESSMENT
       - Keyword optimization
       - Machine readability
       - Standard section headings
       - File format considerations

    5. INDUSTRY STANDARDS COMPLIANCE
       - Field-specific requirements adherence
       - Professional standards alignment
       - Current market expectations

    6. STRENGTHS IDENTIFICATION
       - Top 3-5 strongest points
       - Unique value propositions
       - Competitive advantages

    7. IMPROVEMENT AREAS
       - Critical weaknesses to address
       - Missing information or sections
       - Content gaps to fill

    8. SPECIFIC RECOMMENDATIONS
       - Actionable improvement suggestions
       - Content addition/removal advice
       - formatting enhancements
       - Section reorganization suggestions

    9. MARKETABILITY ASSESSMENT
       - Current job market fit
       - Interview likelihood
       - Salary negotiation potential
       - Career level appropriateness

    10. FINAL VERDICT & NEXT STEPS
        - Ready for submission? (Yes/No/With modifications)
        - Priority improvements (Top 3)
        - Timeline for revisions
        - Success probability estimation

    Additional Context: {f"Target Role: {target_role}" if target_role else "General CV Analysis"}
    {f"Industry Focus: {industry}" if industry else ""}

    Please provide specific, actionable feedback that will help improve this CV's effectiveness in today's competitive job market.
    Use bullet points for clarity and include examples where applicable.
    """
    
    @staticmethod
    def create_quick_score_prompt(cv_text: str) -> str:
        """
        Create prompt for quick CV scoring.
        
        Args:
            cv_text (str): CV text (truncated for quick analysis)
            
        Returns:
            str: Prompt for quick scoring
        """
        return f"""
    As an expert CV evaluator, provide a quick numerical assessment of this CV on a scale of 1-10 (where 10 is excellent).

    CV Content: {cv_text[:2000]}...  

    Consider:
    - Professional presentation
    - Content quality and relevance
    - Structure and organization
    - Achievement quantification
    - Industry standards compliance

    Respond with only:
    - A number (1-10)
    - One sentence explanation
    
    Format: "Score: X/10 - [brief reason]"
    """


class CVAnalysisEngine(CVAnalyzer):
    """
    Main CV Analysis Engine that orchestrates the entire analysis process.
    """
    
    def __init__(self, api_key: str):
        """Initialize the CV Analysis Engine."""
        super().__init__(api_key)
        self.pdf_processor = PDFProcessor()
        self.prompt_engineer = PromptEngineering()
    
    def analyze_cv_comprehensive(self, cv_text: str, target_role: Optional[str] = None, 
                               industry: Optional[str] = None) -> str:
        """
        Perform comprehensive CV analysis using Gemini AI.
        
        Args:
            cv_text (str): Extracted CV text
            target_role (Optional[str]): Target job role
            industry (Optional[str]): Target industry
            
        Returns:
            str: Comprehensive analysis results
        """
        try:
            prompt = self.prompt_engineer.create_comprehensive_analysis_prompt(
                cv_text, target_role, industry
            )
            
            response = self.gemini_model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=0.3,
                    top_p=0.8,
                    max_output_tokens=4000,
                )
            )
            
            return response.text
            
        except Exception as e:
            return f"Error analyzing CV with Gemini API: {e}"
    
    def get_quick_score(self, cv_text: str) -> str:
        """
        Get a quick numerical score for the CV.
        
        Args:
            cv_text (str): CV text for quick evaluation
            
        Returns:
            str: Quick score assessment
        """
        try:
            prompt = self.prompt_engineer.create_quick_score_prompt(cv_text)
            
            response = self.quick_model.generate_content(
                prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=0.2,
                    max_output_tokens=100,
                )
            )
            return response.text.strip()
        except Exception as e:
            return f"Score: Unable to calculate - {e}"


class CVAnalyzerApp:
    """
    Main application class that handles the user interface and orchestrates CV analysis.
    """
    
    def __init__(self, api_key: str):
        """
        Initialize the CV Analyzer Application.
        
        Args:
            api_key (str): Google Gemini API key
        """
        self.analyzer = CVAnalysisEngine(api_key)
        self.pdf_processor = PDFProcessor()
    
    def display_header(self) -> None:
        """Display application header."""
        print("=" * 60)
        print("🎯 PROFESSIONAL CV ANALYZER (OOP Version)")
        print("   Powered by Gemini AI & Advanced Prompt Engineering")
        print("=" * 60)
    
    def find_and_select_cv(self) -> Optional[Path]:
        """
        Find and let user select CV file from the directory.
        
        Returns:
            Optional[Path]: Selected CV file path or None
        """
        cv_folder = Path(__file__).parent
        print(f"\n📁 Looking for PDF files in: {cv_folder}")
        
        pdf_files = self.pdf_processor.find_pdf_files(cv_folder)
        
        if not pdf_files:
            print("\n❌ No PDF files found in the cv_analyser folder.")
            print("Please add your CV in PDF format to this folder and run again.")
            return None
        
        if len(pdf_files) == 1:
            cv_file = pdf_files[0]
            print(f"\n📄 Found CV: {cv_file.name}")
            return cv_file
        else:
            print(f"\n📄 Found {len(pdf_files)} PDF files:")
            for i, file in enumerate(pdf_files, 1):
                print(f"   {i}. {file.name}")
            
            while True:
                try:
                    choice = int(input("\n📝 Select CV to analyze (number): ")) - 1
                    if 0 <= choice < len(pdf_files):
                        return pdf_files[choice]
                    else:
                        print("❌ Invalid selection. Please try again.")
                except (ValueError, EOFError):
                    print("❌ Please enter a valid number.")
                    return pdf_files[0] if pdf_files else None
    
    def get_analysis_context(self) -> tuple[Optional[str], Optional[str]]:
        """
        Get additional context for CV analysis.
        
        Returns:
            tuple: (target_role, industry)
        """
        print("\n🎯 Optional: Provide additional context for better analysis")
        try:
            target_role = input("Target job role (press Enter to skip): ").strip()
            industry = input("Target industry (press Enter to skip): ").strip()
            return (target_role if target_role else None, 
                   industry if industry else None)
        except EOFError:
            print("\n📝 Using default analysis settings...")
            return None, None
    
    def run_analysis(self) -> None:
        """Main method to run the CV analysis process."""
        self.display_header()
        
        # Find and select CV
        cv_file = self.find_and_select_cv()
        if not cv_file:
            return
        
        # Get analysis context
        target_role, industry = self.get_analysis_context()
        
        # Extract text from CV
        print(f"\n⏳ Extracting text from {cv_file.name}...")
        cv_text = self.pdf_processor.extract_text_from_pdf(cv_file)
        
        if not cv_text:
            print("❌ Failed to extract text from PDF. Please check the file.")
            return
        
        if len(cv_text.strip()) < 100:
            print("⚠️  Warning: Very little text extracted. The PDF might be image-based.")
            print("Consider using a text-based PDF or OCR software.")
        
        # Get quick score first
        print("\n⏳ Getting quick assessment...")
        quick_score = self.analyzer.get_quick_score(cv_text)
        print(f"\n🎯 QUICK ASSESSMENT: {quick_score}")
        
        # Perform comprehensive analysis
        print("\n⏳ Performing comprehensive CV analysis...")
        print("   This may take 30-60 seconds for detailed evaluation...")
        
        analysis = self.analyzer.analyze_cv_comprehensive(cv_text, target_role, industry)
        
        # Display results
        self.display_results(analysis)
    
    def display_results(self, analysis: str) -> None:
        """
        Display the analysis results.
        
        Args:
            analysis (str): Analysis results to display
        """
        print("\n" + "=" * 60)
        print("📊 COMPREHENSIVE CV ANALYSIS REPORT")
        print("=" * 60)
        print(analysis)
        print("\n" + "=" * 60)
        print("✅ Analysis Complete!")
        print("💡 Tip: Save this feedback and work on the recommended improvements.")
        print("=" * 60)


def main():
    """Main entry point for the CV analyzer application."""
    # API Key configuration
    GEMINI_API_KEY = "AIzaSyBqNUxgGEQ01DW17PqlwMCM_K1Ts08-TvY"
    
    try:
        # Create and run the CV analyzer application
        app = CVAnalyzerApp(GEMINI_API_KEY)
        app.run_analysis()
    except Exception as e:
        print(f"❌ Application Error: {e}")
        print("Please check your API key and internet connection.")


if __name__ == "__main__":
    main()