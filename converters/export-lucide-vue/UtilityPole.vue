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
    <path d="M12 2v20" />
    <path d="M2 5h20" />
    <path d="M3 3v2" />
    <path d="M7 3v2" />
    <path d="M17 3v2" />
    <path d="M21 3v2" />
    <path d="m19 5-7 7-7-7" />
  </svg>
</template>

<script setup>
const props = defineProps({
  size: { type: [String, Number], default: 24 },
  stroke: { type: [String, Number], default: 1.5 },
});
</script>

<style lang="scss" scoped></style>