import requests
import json
import time
'''
response = requests.get("https://api.wynncraft.com/v2/recipe/list")
with open("mats.json", "w") as outfile:
    outfile.write(json.dumps(response.json()))'''

recipes = ["Boots-3-5", "Boots-5-7", "Bow-1-3", "Boots-7-9", "Bow-3-5", "Bow-5-7", "Bow-7-9", "Bracelet-3-5", "Bracelet-5-7", "Bracelet-1-3", "Chestplate-1-3", "Chestplate-3-5", "Chestplate-7-9", "Chestplate-5-7", "Dagger-1-3", "Dagger-3-5", "Dagger-5-7", "Bracelet-7-9", "Dagger-7-9", "Food-3-5", "Food-1-3", "Food-5-7", "Food-7-9", "Helmet-1-3", "Helmet-3-5", "Helmet-7-9", "Helmet-5-7", "Necklace-3-5", "Necklace-1-3", "Necklace-7-9", "Necklace-5-7", "Pants-1-3", "Pants-3-5", "Pants-5-7", "Pants-7-9", "Potion-1-3", "Potion-3-5", "Potion-5-7", "Relik-1-3", "Potion-7-9", "Relik-5-7", "Relik-3-5", "Relik-7-9", "Boots-1-3", "Ring-3-5", "Ring-5-7", "Ring-7-9", "Scroll-1-3", "Scroll-3-5", "Scroll-5-7", "Scroll-7-9", "Spear-1-3", "Spear-3-5", "Spear-5-7", "Spear-7-9", "Wand-1-3", "Wand-3-5", "Wand-5-7", "Wand-7-9", "Boots-10-13", "Boots-13-15", "Boots-15-17", "Boots-17-19", "Bow-10-13", "Bow-13-15", "Bracelet-10-13", "Bracelet-13-15", "Bracelet-15-17", "Bow-17-19", "Bracelet-17-19", "Chestplate-10-13", "Chestplate-13-15", "Chestplate-15-17", "Bow-15-17", "Dagger-10-13", "Dagger-13-15", "Chestplate-17-19", "Dagger-17-19", "Food-13-15", "Food-15-17", "Food-10-13", "Food-17-19", "Helmet-10-13", "Helmet-13-15", "Helmet-15-17", "Helmet-17-19", "Necklace-10-13", "Dagger-15-17", "Necklace-15-17", "Necklace-17-19", "Pants-10-13", "Pants-13-15", "Pants-15-17", "Pants-17-19", "Potion-10-13", "Potion-13-15", "Potion-15-17", "Relik-10-13", "Relik-13-15", "Relik-15-17", "Relik-17-19", "Ring-10-13", "Ring-13-15", "Ring-15-17", "Ring-17-19", "Scroll-10-13", "Potion-17-19", "Scroll-13-15", "Scroll-15-17", "Spear-10-13", "Scroll-17-19", "Spear-13-15", "Spear-15-17", "Spear-17-19", "Wand-10-13", "Wand-13-15", "Wand-15-17", "Wand-17-19", "Boots-20-23", "Boots-23-25", "Boots-25-27", "Bow-23-25", "Bow-20-23", "Boots-27-29", "Bow-25-27", "Bow-27-29", "Bracelet-20-23", "Bracelet-23-25", "Bracelet-25-27", "Bracelet-27-29", "Chestplate-23-25", "Chestplate-25-27", "Chestplate-20-23", "Chestplate-27-29", "Dagger-20-23", "Dagger-23-25", "Dagger-25-27", "Dagger-27-29", "Food-20-23", "Food-25-27", "Food-27-29", "Helmet-20-23", "Food-23-25", "Helmet-23-25", "Helmet-27-29", "Helmet-25-27", "Necklace-20-23", "Necklace-23-25", "Necklace-27-29", "Pants-20-23", "Necklace-25-27", "Pants-23-25", "Pants-25-27", "Pants-27-29", "Potion-20-23", "Potion-23-25", "Potion-27-29", "Potion-25-27", "Relik-20-23", "Relik-23-25", "Relik-25-27", "Relik-27-29", "Ring-20-23", "Ring-23-25", "Ring-25-27", "Ring-27-29", "Scroll-20-23", "Scroll-23-25", "Scroll-25-27", "Scroll-27-29", "Spear-20-23", "Spear-23-25", "Spear-25-27", "Spear-27-29", "Wand-20-23", "Wand-23-25", "Wand-25-27", "Wand-27-29", "Boots-30-33", "Boots-33-35", "Boots-35-37", "Boots-37-39", "Bow-30-33", "Bow-33-35", "Bow-35-37", "Necklace-13-15", "Bow-37-39", "Bracelet-30-33", "Bracelet-33-35", "Bracelet-35-37", "Bracelet-37-39", "Chestplate-30-33", "Chestplate-35-37", "Chestplate-33-35", "Dagger-30-33", "Chestplate-37-39", "Dagger-35-37", "Dagger-37-39", "Food-30-33", "Dagger-33-35", "Food-33-35", "Food-35-37", "Food-37-39", "Helmet-30-33", "Helmet-33-35", "Helmet-35-37", "Helmet-37-39", "Necklace-30-33", "Necklace-33-35", "Necklace-35-37", "Necklace-37-39", "Pants-33-35", "Pants-30-33", "Pants-35-37", "Pants-37-39", "Potion-30-33", "Potion-33-35", "Potion-35-37", "Potion-37-39", "Relik-30-33", "Relik-33-35", "Relik-35-37", "Ring-30-33", "Relik-37-39", "Ring-33-35", "Ring-35-37", "Ring-37-39", "Scroll-30-33", "Scroll-33-35", "Scroll-35-37", "Scroll-37-39", "Spear-30-33", "Spear-33-35", "Spear-35-37", "Spear-37-39", "Wand-30-33", "Wand-33-35", "Wand-35-37", "Boots-40-43", "Wand-37-39", "Boots-45-47", "Boots-47-49", "Boots-43-45", "Bow-40-43", "Bow-47-49", "Bow-43-45", "Bracelet-40-43", "Bow-45-47", "Bracelet-45-47", "Bracelet-47-49", "Chestplate-43-45", "Bracelet-43-45", "Chestplate-40-43", "Chestplate-45-47", "Dagger-40-43", "Chestplate-47-49", "Dagger-43-45", "Dagger-47-49", "Dagger-45-47", "Food-40-43", "Food-43-45", "Food-45-47", "Food-47-49", "Helmet-40-43", "Helmet-43-45", "Helmet-45-47", "Necklace-40-43", "Necklace-43-45", "Necklace-45-47", "Helmet-47-49", "Necklace-47-49", "Pants-40-43", "Pants-43-45", "Pants-45-47", "Pants-47-49", "Potion-43-45", "Potion-45-47", "Relik-40-43", "Potion-47-49", "Potion-40-43", "Relik-45-47", "Ring-40-43", "Relik-43-45", "Ring-45-47", "Relik-47-49", "Ring-43-45", "Ring-47-49", "Scroll-40-43", "Scroll-43-45", "Scroll-45-47", "Scroll-47-49", "Spear-43-45", "Spear-40-43", "Spear-45-47", "Spear-47-49", "Wand-40-43", "Wand-43-45", "Wand-45-47", "Wand-47-49", "Boots-50-53", "Boots-53-55", "Boots-55-57", "Boots-57-59", "Bow-50-53", "Bow-55-57", "Bow-53-55", "Bow-57-59", "Bracelet-50-53", "Bracelet-53-55", "Bracelet-55-57", "Bracelet-57-59", "Chestplate-50-53", "Chestplate-53-55", "Chestplate-55-57", "Chestplate-57-59", "Dagger-50-53", "Dagger-53-55", "Dagger-55-57", "Food-50-53", "Food-53-55", "Food-55-57", "Dagger-57-59", "Food-57-59", "Helmet-50-53", "Helmet-53-55", "Helmet-55-57", "Helmet-57-59", "Necklace-50-53", "Necklace-57-59", "Necklace-53-55", "Necklace-55-57", "Pants-53-55", "Pants-55-57", "Pants-57-59", "Potion-53-55", "Potion-50-53", "Potion-55-57", "Relik-50-53", "Pants-50-53", "Relik-53-55", "Potion-57-59", "Relik-55-57", "Relik-57-59", "Ring-50-53", "Ring-53-55", "Ring-55-57", "Ring-57-59", "Scroll-50-53", "Scroll-53-55", "Scroll-57-59", "Scroll-55-57", "Spear-50-53", "Spear-53-55", "Spear-55-57", "Wand-50-53", "Spear-57-59", "Wand-55-57", "Wand-53-55", "Wand-57-59", "Boots-60-63", "Boots-65-67", "Boots-63-65", "Boots-67-69", "Bow-60-63", "Bow-63-65", "Bow-67-69", "Bow-65-67", "Bracelet-63-65", "Bracelet-60-63", "Bracelet-65-67", "Bracelet-67-69", "Chestplate-63-65", "Chestplate-60-63", "Chestplate-65-67", "Chestplate-67-69", "Dagger-60-63", "Dagger-63-65", "Dagger-65-67", "Dagger-67-69", "Food-60-63", "Food-63-65", "Food-67-69", "Helmet-60-63", "Helmet-63-65", "Food-65-67", "Helmet-65-67", "Helmet-67-69", "Necklace-60-63", "Necklace-63-65", "Necklace-65-67", "Necklace-67-69", "Pants-63-65", "Pants-60-63", "Pants-65-67", "Pants-67-69", "Potion-60-63", "Potion-63-65", "Potion-67-69", "Relik-63-65", "Relik-65-67", "Potion-65-67", "Relik-67-69", "Relik-60-63", "Ring-60-63", "Ring-65-67", "Ring-63-65", "Ring-67-69", "Scroll-60-63", "Scroll-63-65", "Scroll-67-69", "Scroll-65-67", "Spear-63-65", "Spear-60-63", "Spear-67-69", "Wand-60-63", "Wand-63-65", "Spear-65-67", "Wand-65-67", "Wand-67-69", "Boots-70-73", "Boots-73-75", "Boots-77-79", "Boots-75-77", "Bow-75-77", "Bow-73-75", "Bracelet-70-73", "Bow-77-79", "Bracelet-73-75", "Bow-70-73", "Bracelet-75-77", "Chestplate-70-73", "Bracelet-77-79", "Chestplate-73-75", "Chestplate-75-77", "Chestplate-77-79", "Dagger-70-73", "Dagger-73-75", "Dagger-75-77", "Food-70-73", "Dagger-77-79", "Food-73-75", "Food-75-77", "Food-77-79", "Helmet-70-73", "Helmet-73-75", "Helmet-75-77", "Helmet-77-79", "Necklace-70-73", "Necklace-73-75", "Necklace-75-77", "Necklace-77-79", "Pants-73-75", "Pants-75-77", "Pants-77-79", "Pants-70-73", "Potion-70-73", "Potion-73-75", "Potion-75-77", "Potion-77-79", "Relik-70-73", "Relik-73-75", "Relik-75-77", "Relik-77-79", "Ring-70-73", "Ring-73-75", "Ring-75-77", "Ring-77-79", "Scroll-70-73", "Scroll-73-75", "Scroll-75-77", "Scroll-77-79", "Spear-70-73", "Spear-73-75", "Spear-75-77", "Spear-77-79", "Wand-70-73", "Wand-73-75", "Wand-75-77", "Wand-77-79", "Boots-80-83", "Boots-83-85", "Boots-85-87", "Boots-87-89", "Bow-83-85", "Bow-85-87", "Bow-80-83", "Bracelet-83-85", "Bracelet-80-83", "Bracelet-85-87", "Bow-87-89", "Bracelet-87-89", "Chestplate-80-83", "Chestplate-83-85", "Chestplate-85-87", "Chestplate-87-89", "Dagger-83-85", "Dagger-80-83", "Dagger-85-87", "Dagger-87-89", "Food-83-85", "Food-80-83", "Food-85-87", "Food-87-89", "Helmet-80-83", "Helmet-83-85", "Helmet-85-87", "Helmet-87-89", "Necklace-80-83", "Necklace-83-85", "Necklace-85-87", "Necklace-87-89", "Pants-80-83", "Pants-83-85", "Pants-85-87", "Pants-87-89", "Potion-80-83", "Potion-83-85", "Potion-85-87", "Potion-87-89", "Relik-80-83", "Relik-83-85", "Relik-85-87", "Ring-83-85", "Relik-87-89", "Ring-85-87", "Ring-80-83", "Ring-87-89", "Scroll-80-83", "Scroll-85-87", "Scroll-83-85", "Spear-80-83", "Scroll-87-89", "Spear-85-87", "Wand-80-83", "Spear-87-89", "Wand-83-85", "Wand-85-87", "Wand-87-89", "Spear-83-85", "Boots-93-95", "Boots-95-97", "Boots-90-93", "Boots-97-99", "Bow-90-93", "Bow-93-95", "Bow-95-97", "Bow-97-99", "Bracelet-90-93", "Bracelet-93-95", "Bracelet-97-99", "Chestplate-90-93", "Chestplate-93-95", "Bracelet-95-97", "Chestplate-95-97", "Ring-1-3", "Chestplate-97-99", "Dagger-93-95", "Dagger-90-93", "Dagger-95-97", "Dagger-97-99", "Food-90-93", "Food-93-95", "Food-95-97", "Food-97-99", "Helmet-90-93", "Helmet-93-95", "Helmet-95-97", "Helmet-97-99", "Necklace-93-95", "Necklace-95-97", "Necklace-97-99", "Pants-90-93", "Necklace-90-93", "Pants-93-95", "Pants-97-99", "Potion-90-93", "Potion-93-95", "Potion-95-97", "Relik-90-93", "Potion-97-99", "Relik-93-95", "Relik-95-97", "Ring-90-93", "Ring-95-97", "Ring-93-95", "Scroll-90-93", "Scroll-93-95", "Ring-97-99", "Scroll-95-97", "Spear-90-93", "Spear-93-95", "Spear-95-97", "Spear-97-99", "Relik-97-99", "Pants-95-97", "Wand-90-93", "Scroll-97-99", "Wand-93-95", "Wand-95-97", "Wand-97-99", "Boots-100-103", "Bow-100-103", "Bracelet-100-103", "Chestplate-100-103", "Dagger-100-103", "Necklace-100-103", "Potion-100-103", "Relik-100-103", "Ring-100-103", "Scroll-100-103", "Spear-100-103", "Pants-100-103", "Boots-103-105", "Bow-103-105", "Bracelet-103-105", "Chestplate-103-105", "Dagger-103-105", "Food-103-105", "Helmet-103-105", "Food-100-103", "Pants-103-105", "Potion-103-105", "Relik-103-105", "Wand-100-103", "Ring-103-105", "Necklace-103-105", "Scroll-103-105", "Spear-103-105", "Wand-103-105", "Helmet-100-103"]
#recipes = ["Boots-3-5", "Boots-5-7", "Bow-1-3", "Boots-7-9", "Bow-3-5", "Bow-5-7", "Bow-7-9", "Bracelet-3-5", "Bracelet-5-7", "Bracelet-1-3", "Chestplate-1-3", "Chestplate-3-5", "Chestplate-7-9", "Chestplate-5-7", "Dagger-1-3", "Dagger-3-5", "Dagger-5-7", "Bracelet-7-9", "Dagger-7-9", "Food-3-5", "Food-1-3", "Food-5-7", "Food-7-9", "Helmet-1-3", "Helmet-3-5", "Helmet-7-9", "Helmet-5-7", "Necklace-3-5", "Necklace-1-3", "Necklace-7-9", "Necklace-5-7", "Pants-1-3", "Pants-3-5", "Pants-5-7", "Pants-7-9", "Potion-1-3", "Potion-3-5", "Potion-5-7", "Relik-1-3", "Potion-7-9", "Relik-5-7", "Relik-3-5", "Relik-7-9", "Boots-1-3", "Ring-3-5", "Ring-5-7", "Ring-7-9", "Scroll-1-3", "Scroll-3-5", "Scroll-5-7", "Scroll-7-9", "Spear-1-3", "Spear-3-5", "Spear-5-7", "Spear-7-9", "Wand-1-3", "Wand-3-5", "Wand-5-7", "Wand-7-9", "Boots-10-13", "Boots-13-15", "Boots-15-17", "Boots-17-19", "Bow-10-13", "Bow-13-15", "Bracelet-10-13", "Bracelet-13-15", "Bracelet-15-17", "Bow-17-19", "Bracelet-17-19", "Chestplate-10-13", "Chestplate-13-15", "Chestplate-15-17", "Bow-15-17", "Dagger-10-13", "Dagger-13-15", "Chestplate-17-19", "Dagger-17-19", "Food-13-15", "Food-15-17", "Food-10-13", "Food-17-19", "Helmet-10-13", "Helmet-13-15", "Helmet-15-17", "Helmet-17-19", "Necklace-10-13", "Dagger-15-17", "Necklace-15-17", "Necklace-17-19", "Pants-10-13", "Pants-13-15", "Pants-15-17", "Pants-17-19", "Potion-10-13", "Potion-13-15", "Potion-15-17", "Relik-10-13", "Relik-13-15", "Relik-15-17", "Relik-17-19", "Ring-10-13", "Ring-13-15", "Ring-15-17", "Ring-17-19", "Scroll-10-13", "Potion-17-19", "Scroll-13-15", "Scroll-15-17", "Spear-10-13", "Scroll-17-19", "Spear-13-15", "Spear-15-17", "Spear-17-19", "Wand-10-13", "Wand-13-15", "Wand-15-17", "Wand-17-19", "Boots-20-23", "Boots-23-25", "Boots-25-27", "Bow-23-25", "Bow-20-23", "Boots-27-29", "Bow-25-27", "Bow-27-29", "Bracelet-20-23", "Bracelet-23-25", "Bracelet-25-27", "Bracelet-27-29", "Chestplate-23-25", "Chestplate-25-27", "Chestplate-20-23", "Chestplate-27-29", "Dagger-20-23", "Dagger-23-25", "Dagger-25-27", "Dagger-27-29", "Food-20-23", "Food-25-27", "Food-27-29", "Helmet-20-23", "Food-23-25", "Helmet-23-25", "Helmet-27-29", "Helmet-25-27", "Necklace-20-23", "Necklace-23-25", "Necklace-27-29", "Pants-20-23", "Necklace-25-27", "Pants-23-25", "Pants-25-27", "Pants-27-29", "Potion-20-23", "Potion-23-25", "Potion-27-29", "Potion-25-27", "Relik-20-23", "Relik-23-25", "Relik-25-27", "Relik-27-29", "Ring-20-23", "Ring-23-25", "Ring-25-27", "Ring-27-29", "Scroll-20-23", "Scroll-23-25", "Scroll-25-27", "Scroll-27-29", "Spear-20-23", "Spear-23-25", "Spear-25-27", "Spear-27-29", "Wand-20-23", "Wand-23-25", "Wand-25-27", "Wand-27-29", "Boots-30-33", "Boots-33-35", "Dagger-33-35", "Food-33-35", "Food-35-37", "Food-37-39", "Helmet-30-33", "Helmet-33-35", "Helmet-35-37", "Helmet-37-39", "Necklace-30-33", "Necklace-33-35", "Necklace-35-37", "Necklace-37-39", "Pants-33-35", "Pants-30-33", "Pants-35-37", "Pants-37-39", "Potion-30-33", "Potion-33-35", "Potion-35-37", "Potion-37-39", "Relik-30-33", "Relik-33-35", "Relik-35-37", "Ring-30-33", "Relik-37-39", "Ring-33-35", "Ring-35-37", "Ring-37-39", "Scroll-30-33", "Scroll-33-35", "Scroll-35-37", "Scroll-37-39", "Spear-30-33", "Spear-33-35", "Spear-35-37", "Spear-37-39", "Wand-30-33", "Wand-33-35", "Wand-35-37", "Boots-40-43", "Wand-37-39", "Boots-45-47", "Boots-47-49", "Boots-43-45", "Bow-40-43", "Bow-47-49", "Bow-43-45", "Bracelet-40-43", "Bow-45-47", "Bracelet-45-47", "Bracelet-47-49", "Chestplate-43-45", "Bracelet-43-45", "Chestplate-40-43", "Chestplate-45-47", "Dagger-40-43", "Chestplate-47-49", "Dagger-43-45", "Dagger-47-49", "Dagger-45-47", "Food-40-43", "Food-43-45", "Food-45-47", "Food-47-49", "Helmet-40-43", "Helmet-43-45", "Helmet-45-47", "Necklace-40-43", "Necklace-43-45", "Necklace-45-47", "Helmet-47-49", "Necklace-47-49", "Pants-40-43", "Pants-43-45", "Pants-45-47", "Pants-47-49", "Potion-43-45", "Potion-45-47", "Relik-40-43", "Potion-47-49", "Potion-40-43", "Relik-45-47", "Ring-40-43", "Relik-43-45", "Ring-45-47", "Relik-47-49", "Ring-43-45", "Ring-47-49", "Scroll-40-43", "Scroll-43-45", "Scroll-45-47", "Scroll-47-49", "Spear-43-45", "Spear-40-43", "Spear-45-47", "Spear-47-49", "Wand-40-43", "Wand-43-45", "Wand-45-47", "Wand-47-49", "Boots-50-53", "Boots-53-55", "Boots-55-57", "Boots-57-59", "Bow-50-53", "Bow-55-57", "Bow-53-55", "Bow-57-59", "Bracelet-50-53", "Bracelet-53-55", "Bracelet-55-57", "Bracelet-57-59", "Chestplate-50-53", "Chestplate-53-55", "Chestplate-55-57", "Chestplate-57-59", "Dagger-50-53", "Dagger-53-55", "Dagger-55-57", "Food-50-53", "Food-53-55", "Food-55-57", "Dagger-57-59", "Food-57-59", "Helmet-50-53", "Helmet-53-55", "Helmet-55-57", "Helmet-57-59", "Necklace-50-53", "Necklace-57-59", "Necklace-53-55", "Necklace-55-57", "Pants-53-55", "Pants-55-57", "Pants-57-59", "Potion-53-55", "Potion-50-53", "Potion-55-57", "Relik-50-53", "Pants-50-53", "Relik-53-55", "Potion-57-59", "Relik-55-57", "Relik-57-59", "Ring-50-53", "Ring-53-55", "Ring-55-57", "Ring-57-59", "Scroll-50-53", "Scroll-53-55", "Scroll-57-59", "Scroll-55-57", "Spear-50-53", "Spear-53-55", "Spear-55-57", "Wand-50-53", "Spear-57-59", "Wand-55-57", "Wand-53-55", "Wand-57-59", "Boots-60-63", "Boots-65-67", "Boots-63-65", "Boots-67-69", "Bow-60-63", "Bow-63-65", "Bow-67-69", "Bow-65-67", "Bracelet-63-65", "Bracelet-60-63", "Bracelet-65-67", "Bracelet-67-69", "Chestplate-63-65", "Chestplate-60-63", "Chestplate-65-67", "Chestplate-67-69", "Dagger-60-63", "Dagger-63-65", "Dagger-65-67", "Dagger-67-69", "Spear-60-63", "Spear-67-69", "Wand-60-63", "Wand-63-65", "Spear-65-67", "Wand-65-67", "Wand-67-69", "Boots-70-73", "Boots-73-75", "Boots-77-79", "Boots-75-77", "Bow-75-77", "Bow-73-75", "Bracelet-70-73", "Bow-77-79", "Bracelet-73-75", "Bow-70-73", "Bracelet-75-77", "Chestplate-70-73", "Bracelet-77-79", "Chestplate-73-75", "Chestplate-75-77", "Chestplate-77-79", "Dagger-70-73", "Dagger-73-75", "Dagger-75-77", "Food-70-73", "Dagger-77-79", "Food-73-75", "Food-75-77", "Food-77-79", "Helmet-70-73", "Helmet-73-75", "Helmet-75-77", "Helmet-77-79", "Necklace-70-73", "Necklace-73-75", "Necklace-75-77", "Necklace-77-79", "Pants-73-75", "Pants-75-77", "Pants-77-79", "Pants-70-73", "Potion-70-73", "Potion-73-75", "Potion-75-77", "Potion-77-79", "Relik-70-73", "Relik-73-75", "Relik-75-77", "Relik-77-79", "Ring-70-73", "Ring-73-75", "Ring-75-77", "Ring-77-79", "Scroll-70-73", "Scroll-73-75", "Scroll-75-77", "Scroll-77-79", "Spear-70-73", "Spear-73-75", "Spear-75-77", "Spear-77-79", "Wand-70-73", "Wand-73-75", "Wand-75-77", "Wand-77-79", "Boots-80-83", "Boots-83-85", "Boots-85-87", "Boots-87-89", "Bow-83-85", "Bow-85-87", "Bow-80-83", "Bracelet-83-85", "Bracelet-80-83", "Bracelet-85-87", "Bow-87-89", "Bracelet-87-89", "Chestplate-80-83", "Chestplate-83-85", "Chestplate-85-87", "Chestplate-87-89", "Dagger-83-85", "Dagger-80-83", "Dagger-85-87", "Dagger-87-89", "Food-83-85", "Food-80-83", "Food-85-87", "Food-87-89", "Helmet-80-83", "Helmet-83-85", "Helmet-85-87", "Helmet-87-89", "Necklace-80-83", "Necklace-83-85", "Necklace-85-87", "Necklace-87-89", "Pants-80-83", "Pants-83-85", "Pants-85-87", "Pants-87-89", "Potion-80-83", "Potion-83-85", "Potion-85-87", "Potion-87-89", "Relik-80-83", "Relik-83-85", "Relik-85-87", "Ring-83-85", "Relik-87-89", "Ring-85-87", "Ring-80-83", "Ring-87-89", "Scroll-80-83", "Scroll-85-87", "Scroll-83-85", "Spear-80-83", "Scroll-87-89", "Spear-85-87", "Wand-80-83", "Spear-87-89", "Wand-83-85", "Wand-85-87", "Wand-87-89", "Spear-83-85", "Boots-93-95", "Boots-95-97", "Boots-90-93", "Boots-97-99", "Bow-90-93", "Bow-93-95", "Bow-95-97", "Bow-97-99", "Bracelet-90-93", "Bracelet-93-95", "Bracelet-97-99", "Chestplate-90-93", "Chestplate-93-95", "Bracelet-95-97", "Chestplate-95-97", "Ring-1-3", "Chestplate-97-99", "Dagger-93-95", "Dagger-90-93", "Dagger-95-97", "Dagger-97-99", "Food-90-93", "Food-93-95", "Food-95-97", "Food-97-99", "Helmet-90-93", "Helmet-93-95", "Helmet-95-97", "Helmet-97-99", "Necklace-93-95", "Necklace-95-97", "Necklace-97-99", "Pants-90-93", "Necklace-90-93", "Pants-93-95", "Pants-97-99", "Potion-90-93", "Potion-93-95", "Potion-95-97", "Relik-90-93", "Potion-97-99", "Relik-93-95", "Relik-95-97", "Ring-90-93", "Ring-95-97", "Ring-93-95", "Scroll-90-93", "Scroll-93-95", "Ring-97-99", "Scroll-95-97", "Spear-90-93", "Spear-93-95", "Spear-95-97", "Spear-97-99", "Relik-97-99", "Pants-95-97", "Wand-90-93", "Scroll-97-99", "Wand-93-95", "Wand-95-97", "Wand-97-99", "Boots-100-103", "Bow-100-103", "Bracelet-100-103", "Chestplate-100-103", "Dagger-100-103", "Necklace-100-103", "Potion-100-103", "Relik-100-103", "Ring-100-103", "Scroll-100-103", "Spear-100-103", "Pants-100-103", "Boots-103-105", "Bow-103-105", "Bracelet-103-105", "Chestplate-103-105", "Dagger-103-105", "Food-103-105", "Helmet-103-105", "Food-100-103", "Pants-103-105", "Potion-103-105", "Relik-103-105", "Wand-100-103", "Ring-103-105", "Necklace-103-105", "Scroll-103-105", "Spear-103-105", "Wand-103-105", "Helmet-100-103"]

arr = []
fail = []
data = []

'''for i in range(330,len(recipes)):
    response = requests.get("https://api.wynncraft.com/v2/recipe/get/" + recipes[i])
    if("message" in response.json()):
        print("failed to get " + recipes[i])
        fail.append(recipes[i])
    else: 
        arr.append(response.json())
    time.sleep(0.2)

with open("temp.json", "w") as outfile:
    json.dump(arr,outfile)'''


with open("mats_clean.json", "w") as outfile:
    json.dump(arr,outfile,indent = 2)

with open("mats_compress.json", "w") as outfile:
    json.dump(arr,outfile)