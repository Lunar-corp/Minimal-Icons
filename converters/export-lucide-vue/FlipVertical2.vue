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
    <path d="m17 3-5 5-5-5h10" />
    <path d="m17 21-5-5-5 5h10" />
    <path d="M4 12H2" />
    <path d="M10 12H8" />
    <path d="M16 12h-2" />
    <path d="M22 12h-2" />
  </svg>
</template>

<script setup>
const props = defineProps({
  size: { type: [String, Number], default: 24 },
  stroke: { type: [String, Number], default: 1.5 },
});
</script>

<style lang="scss" scoped></style>