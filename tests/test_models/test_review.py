#!/usr/bin/python3
"""Testing the user model inheriting from the basemodel"""
import unittest
import models
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Class Review test implementation"""
    def test_review_inherits_from_base_model(self):
        """Testing class review is a subclass of another class"""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_review_default_attributes(self):
        """Testing review default attributes"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_review_attribute_assigments(self):
        """Testing review attributes being assigned information"""
        review = Review()
        review.place_id = "456-789"
        review.user_id = "123-321"
        review.text = "wonderful reception"

        self.assertEqual(review.place_id, "456-789")
        self.assertEqual(review.user_id, "123-321")
        self.assertEqual(review.text, "wonderful reception")

    def test_init_Review(self):
        """Testing if the object is review"""
        object_check = Review()
        self.assertIsInstance(object_check, Review)

    def test_id(self):
        """Testing that id to be unique"""
        first_id = Review()
        second_id = Review()
        self.assertNotEqual(first_id, second_id)

    def test_review_to_dict(self):
        """Testing review attributes in a dictionary"""
        review = Review()
        review.place_id = "456-789"
        review.user_id = "123-321"
        review.text = "wonderful reception"

        review_dict = review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertEqual(review_dict['place_id'], "456-789")
        self.assertEqual(review_dict['user_id'], "123-321")
        self.assertEqual(review_dict['text'], "wonderful reception")
        self.assertEqual(review_dict['__class__'], "Review")

    def test_review_str(self):
        """Testing string representation of the review class"""
        review = Review()
        review.place_id = "456-789"
        review.user_id = "123-321"
        review.text = "wonderful reception"

        string_repr = str(review)
        expected_repr = f"[Review] ({review.id}) {review.__dict__}"
        self.assertEqual(string_repr, expected_repr)

    def test_review_save(self):
        """Testing for updates when saved"""
        review = Review()
        old_updated_at = review.updated_at
        review.save()
        new_updated_at = review.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)


if __name__ == "__main__":
    unittest.main()
