<template>
  <svg
    xmlns="http://www.w3.org/2000/svg"
    :width="size"
    :height="size"
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    :stroke-width="stroke"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <path d="M2 17 17 2" />
    <path d="m2 14 8 8" />
    <path d="m5 11 8 8" />
    <path d="m8 8 8 8" />
    <path d="m11 5 8 8" />
    <path d="m14 2 8 8" />
    <path d="M7 22 22 7" />
  </svg>
</template>

<script setup>
const props = defineProps({
  size: { type: [String, Number], default: 24 },
  stroke: { type: [String, Number], default: 1.5 },
});
</script>

<style lang="scss" scoped></style>