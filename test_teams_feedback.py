#!/usr/bin/env python3
"""
Test script to verify Teams notification functionality with correction details
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from teams_config import send_feedback_notification

def test_like_feedback():
    """Test like feedback notification"""
    print("Testing LIKE feedback notification...")
    
    prediction = {
        'product_line_code': '2JE',
        'cmr_product_line': '2DBioProcessContainers',
        'combined_score': 85.5
    }
    
    result = send_feedback_notification(
        user_email="test.user@thermofisher.com",
        user_name="Test User",
        sku_input="SV50139.06",
        name_input="PKG MATL| COLLAPSIBLE BIN",
        prediction=prediction,
        feedback_type="like"
    )
    
    print(f"Like feedback notification result: {'Success' if result else 'Failed'}")
    return result

def test_dislike_feedback_with_corrections():
    """Test dislike feedback notification with corrections and comments"""
    print("Testing DISLIKE feedback notification with corrections...")
    
    prediction = {
        'product_line_code': '2JE',
        'cmr_product_line': '2DBioProcessContainers',
        'combined_score': 65.2
    }
    
    result = send_feedback_notification(
        user_email="test.user@thermofisher.com",
        user_name="Test User",
        sku_input="SV50139.06",
        name_input="PKG MATL| COLLAPSIBLE BIN",
        prediction=prediction,
        feedback_type="dislike",
        correct_product_line="2MH",
        correct_business_unit="FLEXIBLE SOLUTIONS",
        user_comment="The prediction was incorrect. This should be classified as 3D container based on volume analysis."
    )
    
    print(f"Dislike feedback notification result: {'Success' if result else 'Failed'}")
    return result

def test_dislike_feedback_minimal():
    """Test dislike feedback notification with minimal corrections"""
    print("Testing DISLIKE feedback notification with minimal corrections...")
    
    prediction = {
        'product_line_code': '2JE',
        'cmr_product_line': '2DBioProcessContainers',
        'combined_score': 45.8
    }
    
    result = send_feedback_notification(
        user_email="test.user@thermofisher.com",
        user_name="Test User",
        sku_input="TEST123",
        name_input="Test Product Name",
        prediction=prediction,
        feedback_type="dislike",
        correct_product_line="2PS",
        correct_business_unit=None,  # No business unit correction
        user_comment=None  # No comment
    )
    
    print(f"Minimal dislike feedback notification result: {'Success' if result else 'Failed'}")
    return result

if __name__ == "__main__":
    print("=" * 60)
    print("TESTING TEAMS FEEDBACK NOTIFICATIONS")
    print("=" * 60)
    
    # Test different scenarios
    test1 = test_like_feedback()
    print()
    
    test2 = test_dislike_feedback_with_corrections()
    print()
    
    test3 = test_dislike_feedback_minimal()
    print()
    
    print("=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    print(f"Like feedback test: {'✅ PASSED' if test1 else '❌ FAILED'}")
    print(f"Full dislike feedback test: {'✅ PASSED' if test2 else '❌ FAILED'}")
    print(f"Minimal dislike feedback test: {'✅ PASSED' if test3 else '❌ FAILED'}")
    
    if all([test1, test2, test3]):
        print("\n🎉 All tests passed! Teams notifications are working correctly.")
    else:
        print("\n⚠️  Some tests failed. Please check the Teams webhook configuration.")